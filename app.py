# Description: Flask app for serving the model

# Better printing
from pprint import pprint

# Funcions and constants
from src.models import read_model
from src.const import (
    variable_types,
    fill_na_values,
    model_variables
)
from src.data_processing import preprocess

# Processing
import pandas as pd

# Server
from flask import Flask, request

# Setting app as the name of the Flask instance
app = Flask(__name__)

# Load traiend models and processers
model = read_model("LogisticRegression")
one_hot_encoder = read_model("one_hot_encoder")
scaler = read_model("scaler")

# Defining the route for the server
@app.route("/")

# Defining the function that will be executed when the route of the site is called
def hello_world():
    print(request.headers)

    # It returns this message to let us know that the server is running
    return "Server is running"

# Creation of the route for the requests using Flasks POST method
@app.route("/predict", methods=["POST"])

# Definition of the function that will be executed when the route /predict is called
def predict():

    # Verification that the data sent from the client are received correctly by the server
    print(f"REQUEST: {request.json}")

    # Conversion of json to dataframe
    data = pd.DataFrame(request.json["data"])

    # Filter raw columns in case there is an unexpected variable
    for column in data.columns:
        
        # Drop columns that are not in the model
        if column not in model_variables["raw"]:
            data = data.drop(column, axis=1)
    
    # Check if there are missing variables
    missing_variables = [var for var in model_variables["raw"] if var not in data.columns]

    # Return error if there are missing variables
    if missing_variables:
        return {
            "message": f"Some of the required variables are missing: {missing_variables}"
        }, 400

    # Preprocess the received data
    # Here, the saved processers and values form notebook 8 are used
    X = preprocess(
        data=data,
        fill_na_values=fill_na_values,
        one_hot_encoder=one_hot_encoder,
        scaler=scaler,
        variable_types=variable_types,
        model_variables=model_variables["raw"]
    )

    # Use only varaibles seen during fit to avoid errors
    X = X[model.feature_names_in_]

    # Save the prediction and probability
    prediction = [int(p) for p in model.predict(X)]
    probas = model.predict_proba(X)
    fraud_proba = [float(round(p, 4)) for p in probas[0:,1]]

    # Dictionary with the prediction and probability
    response = {
        "prediction": prediction,
        "probability": fraud_proba,
    }

    # Print the response
    pprint(response)

    return response

# Check if the script is being executed directly and not as an imported module
if __name__ == "__main__":
    # Run the app on port 5000 and with debug mode on
    app.run(port=5000, debug=True)

# If we access the route localhost:5000 we will see the message "Server is running"
