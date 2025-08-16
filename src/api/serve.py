from flask import Flask, request, jsonify
from src.models.predict import make_prediction

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Assuming the input data is a dictionary with the necessary features
    prediction = make_prediction(data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)