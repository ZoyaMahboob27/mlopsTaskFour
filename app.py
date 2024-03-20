from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)
model = load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
