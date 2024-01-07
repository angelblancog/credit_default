from pprint import pprint
from src.models import read_model
from src.data import read_csv
from src.const import (
    variable_types,
    fill_na_values,
    model_variables
)
from src.data_processing import preprocess
import pandas as pd

from flask import Flask, request

app = Flask(__name__)

# Load traiend models and processers
global model
model = read_model("LogisticRegression")

global one_hot_encoder
one_hot_encoder = read_model("one_hot_encoder")

global scaler
scaler = read_model("scaler")


@app.route("/")
def hello_world():
    print(request.headers)

    return "Hello, World!"


@app.route("/predict", methods=["POST"])
def predict():

    # What is being passed to the server
    data = pd.DataFrame(
        {key: [value] for key, value in request.json.items()}
    )

    # Filter raw columns in case there is sometihng unexpected
    data = data[model_variables["raw"]]
    
    # Preprocess data (one hot, scale, etc)
    X = preprocess(
        data=data,
        fill_na_values=fill_na_values,
        one_hot_encoder=one_hot_encoder,
        scaler=scaler,
        variable_types=variable_types,
        model_variables=model_variables["raw"]
    )

    # Use only varaibles seen during fit
    X = X[model.feature_names_in_]

    prediction = model.predict(X)[0]
    probas = model.predict_proba(X)
    fraud_proba = probas[0][1]
    fraud_proba = round(fraud_proba, 4)

    response = {
        "prediction": int(prediction),
        "proba": float(fraud_proba),
        "status": "Paid" if prediction == 0 else "Fraud"
    }

    pprint(response)

    return response

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)