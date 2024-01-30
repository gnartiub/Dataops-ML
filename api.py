from flask import Flask, request, jsonify
import joblib
import ollama

app = Flask(__name__)
regr = joblib.load("model.v1.bin")


def encode_prenom(prenom: str):
    """
        This function encode a given name into a pd.Series.

        For instance alain is encoded [1, 0, 0, 0, 0 ... 1, 0 ...].
    """
    alphabet = "abcdefghijklmnopqrstuvwxyzé-'"
    prenom = prenom.lower()

    return [int(letter in prenom) for letter in alphabet]


@app.route("/predict")
def predict():
    name = request.args.get("name")
    model = request.args.get("model")
    if not model:
        if name:
            sexe = regr.predict([encode_prenom(name)])
            response = {
                "name": name,
                "gender": 'M' if sexe[0] == 0 else 'F',
            }
            return jsonify(response)
        else:
            return jsonify({"error": "You need to pass name as GET parameter."})
    else:
        if name:
            promt = "Classify the name {name} : Man's name or woman's name. If the name is man's, return 'H', if not return 'F'"
            sexe = ollama(prompt)
            response = ollama.chat(model='llama2', messages=[
            {
                'role': 'user',
                'content': promt,
            },
            ])
            response = {
                "name": name,
                "gender": response['message']['content'],
            }
            return jsonify(response)
        else:
            return jsonify({"error": "You need to pass name as GET parameter."})
