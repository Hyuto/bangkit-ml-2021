const get_data = async (batch = 10, seed = 2021) => {
    const trainingUrl = 'https://raw.githubusercontent.com/lmoroney/dlaicourse/master/' + 
                        'TensorFlow%20Deployment/Course%201%20-%20TensorFlow-JS/' + 
                        'Week%201/Exercise/wdbc-train.csv';
    const trainingData = tf.data.csv(trainingUrl, {
        columnConfigs: {
            diagnosis: {
                isLabel: true
            }
        }
    });
    const convertedTrainingData = trainingData.map(({xs, ys}) => {
        return {xs: Object.values(xs), ys: Object.values(ys)};
    }).shuffle(seed).batch(batch);

    const testingUrl = 'https://raw.githubusercontent.com/lmoroney/dlaicourse/master/' + 
                       'TensorFlow%20Deployment/Course%201%20-%20TensorFlow-JS/' + 
                       'Week%201/Exercise/wdbc-test.csv';
    const testingData = tf.data.csv(testingUrl, {
        columnConfigs: {
            diagnosis: {
                isLabel: true
            }
        }
    });
    const convertedTestingData = testingData.map(({xs, ys}) => {
        return {xs: Object.values(xs), ys: Object.values(ys)};
    }).shuffle(seed).batch(batch);

    const numOfFeatures = (await trainingData.columnNames()).length - 1;
    return [numOfFeatures, convertedTrainingData, convertedTestingData];
}

const train = async (model, train, valid) => {
    const log = document.getElementById('log');
    await model.fitDataset(train, {
        epochs: 100,
        validationData: valid,
        callbacks: {
            onEpochEnd: async (epoch, logs) => {
                log.innerText += `Epoch: ${epoch + 1} - loss: ${logs.loss.toFixed(4)}` + 
                                 ` - acc: ${logs.acc.toFixed(4)} - val_loss: ` + 
                                 `${logs.val_loss.toFixed(4)} - val_acc: ` + 
                                 `${logs.val_acc.toFixed(4)}\n`;
                log.scrollTop = log.scrollHeight;
            }
        }
    });
}

const data = get_data();
const model = tf.sequential();
data.then(([numOfFeatures, convertedTrainingData, convertedTestingData]) => {
    model.add(tf.layers.dense({inputShape: [numOfFeatures], activation: "relu", units: 32}))
    model.add(tf.layers.dense({activation: "relu", units: 16}))
    model.add(tf.layers.dense({activation: "sigmoid", units: 1}))
    model.compile({
        loss: "binaryCrossentropy", optimizer: 'rmsprop', metrics: ['acc']
    });
    train(model, convertedTrainingData, convertedTestingData).then(() => {
        model.save('downloads://my_model');
    })
})