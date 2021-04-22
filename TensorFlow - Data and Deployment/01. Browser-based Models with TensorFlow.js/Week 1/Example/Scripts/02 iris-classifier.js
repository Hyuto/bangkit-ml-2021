const get_data = async (batch = 10, seed = 2021) => {
    const csvUrl = 'https://raw.githubusercontent.com/lmoroney/dlaicourse/master/TensorFlow%20Deployment/' + 
                    'Course%201%20-%20TensorFlow-JS/Week%201/Examples/iris.csv';
    const trainingData = tf.data.csv(csvUrl, {
            columnConfigs: {
                species: {
                    isLabel: true
                }
            }
        });

    const numOfFeatures = (await trainingData.columnNames()).length - 1;
    const convertedData = trainingData.map(({xs, ys}) => {
            const labels = [
                ys.species == "setosa" ? 1 : 0,
                ys.species == "virginica" ? 1 : 0,
                ys.species == "versicolor" ? 1 : 0
            ]
            return {xs: Object.values(xs), ys: Object.values(labels)};
        })
        .shuffle(seed)
        .batch(batch);
    
    return [numOfFeatures, convertedData];
}

const train = async (model, data) => {
    const log = document.getElementById('log');
    await model.fitDataset(data, {
        epochs: 100,
        callbacks: {
            onEpochEnd: async (epoch, logs) => {
                log.innerText += `Epoch: ${epoch + 1} - Loss: ${logs.loss.toFixed(5)}\n`;
                log.scrollTop = log.scrollHeight;
            }
        }
    });
}

const data = get_data();
const model = tf.sequential();

data.then((e) => {
    const [numOfFeatures, convertedData] = e;
    model.add(
        tf.layers.dense({inputShape: [numOfFeatures], activation: "sigmoid", units: 5})
    );
    model.add(tf.layers.dense({activation: "softmax", units: 3}));
    model.compile({
        loss: "categoricalCrossentropy", optimizer: tf.train.adam(0.06)
    });
    train(model, convertedData).then(() => {
        // Test Cases: Setosa
        const testVal = tf.tensor2d([4.4, 2.9, 1.4, 0.2], [1, 4]);

        // Versicolor const testVal = tf.tensor2d([6.4, 3.2, 4.5, 1.5], [1, 4]);
        // Virginica const testVal = tf.tensor2d([5.8,2.7,5.1,1.9], [1, 4]);

        const prediction = model.predict(testVal);
        const pIndex = tf.argMax(prediction, axis = 1).dataSync();

        const classNames = ["Setosa", "Virginica", "Versicolor"];

        // alert(prediction)
        alert(classNames[pIndex])
    })
})