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

from flask import Flask, request, Response

app = Flask(__name__)

# Load traiend models and processers
model = read_model("LogisticRegression")
one_hot_encoder = read_model("one_hot_encoder")
scaler = read_model("scaler")


@app.route("/")
def hello_world():
    print(request.headers)

    return "Server is running"


@app.route("/predict", methods=["POST"])
def predict():

    print(f"REQUEST: {request.json}")

    data = pd.DataFrame(request.json["data"])

    # Filter raw columns in case there is sometihng unexpected
    for column in data.columns:
        
        if column not in model_variables["raw"]:
            data = data.drop(column, axis=1)
    
    missing_variables = [var for var in model_variables["raw"] if var not in data.columns]

    if missing_variables:
        return {
            "message": f"Some of the required variables are missing: {missing_variables}"
        }, 400

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

    prediction = [int(p) for p in model.predict(X)]
    probas = model.predict_proba(X)
    fraud_proba = [float(round(p, 4)) for p in probas[0:,1]]

    response = {
        "prediction": prediction,
        "probability": fraud_proba,
    }

    pprint(response)

    return response

if __name__ == "__main__":
    app.run(port=5000, debug=True)