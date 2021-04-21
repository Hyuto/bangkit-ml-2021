const doTraining = async (model) => {
    const log = document.getElementById('log');
    await model.fit(xs, ys, {
        epochs: 500,
        callbacks: {
            onEpochEnd: async (epoch, logs) => {
                log.innerText += `Epoch: ${epoch + 1} Loss: ${logs.loss}\n`;
                log.scrollTop = log.scrollHeight;
            }
        }
    });
}

// Create Model
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));
// Compile model
model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});
model.summary();
// Data
const xs = tf.tensor2d([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], [6, 1]);
const ys = tf.tensor2d([-3.0, -1.0, 2.0, 3.0, 5.0, 7.0], [6, 1]);
// Train
doTraining(model).then(() => {
    alert(model.predict(tf.tensor2d([10], [1, 1])));
});