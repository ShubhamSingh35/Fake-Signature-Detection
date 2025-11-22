from flask import Flask, request, jsonify, render_template
import os
from model.predict import PredictModel

app = Flask(__name__)
model = PredictModel(model_path='model/model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    f = request.files['file']
    save_path = os.path.join('uploads', f.filename)
    os.makedirs('uploads', exist_ok=True)
    f.save(save_path)
    result = model.predict_image(save_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
