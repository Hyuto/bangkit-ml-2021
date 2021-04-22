const load_model = async () => {
    const MODEL_URL = './model/my_model/model.json';
    const model = await tf.loadLayersModel(MODEL_URL);
    return model;
}
const model = load_model();
model.then((m) => {
    tfvis.show.modelSummary({name: 'Model Architecture'}, m);
})