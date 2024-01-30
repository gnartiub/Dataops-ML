import pickle
import joblib
from sklearn.linear_model import LogisticRegression

from flask import Flask, request, jsonify
# /Users/trangbui/Documents/ENSAI 3A/Dataops/MLOps
import string
import pandas as pd

def encode_prenom(prenom: str):
    '''
    
    '''
    alphabet = string.ascii_lowercase + 'é-'
    prenom = prenom.lower()
    
    return pd.Series([letter in prenom for letter in alphabet]).astype(int)

class Predictor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        # Load the logistic regression model from the specified path
        with open(self.model_path, 'rb') as file:
            self.model = joblib.load(file)

    def predict(self, input_data):
        if self.model is None:
            self.load_model()
        # Perform prediction using the loaded model
        prediction = self.model.predict(input_data)
        return prediction

# Example usage:
if __name__ == "__main__":
    model_path = "model.v1.bin"
    predictor = Predictor(model_path)
    predictor.load_model()

    app = Flask(__name__)

    @app.route("/", methods=['GET'])
    def root():
        return {"message": "hello"}

    @app.route('/predict', methods=['GET'])
    def predict():
        name = request.args.get("name")
        if name:
            sexe =  predictor.predict([encode_prenom(name)])
            response = {
                "name": name,
                "response": 'H' if sexe[0] == 0 else 'F',
            }
            return jsonify(response)
        else:
            return jsonify({"error": "No prediction"})
    app.run()
