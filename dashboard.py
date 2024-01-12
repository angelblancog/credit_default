# Description: Dashboard for the credit default predictor

# Libraries
import requests
import streamlit as st
import os

# Processing
import pandas as pd

# Functions
from src.style import highlight_fraud

# Working directory check
print(os.getcwd())

# Model server configuration
HOST = os.getenv("MODEL_SERVER_HOST", "http://localhost")
PORT = os.getenv("MODEL_SERVER_PORT", 5000)
ENDPOINT = os.getenv("MODEL_SERVER_ENDPOINT", "/predict")

# Construction of the server url
url = f"{HOST}:{PORT}{ENDPOINT}"

# Headers for the request
headers = {
    "Content-Type": "application/json",
}

# Page configuration
st.set_page_config(page_title="Credit Default Predictor", 
                   page_icon="logo.jpeg", 
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   menu_items=None)

# Addition of title and subtitle
st.title("Credit Default Predictor")
st.markdown("This app predicts the **Default** probability of a credit card user")

# Tabs for manual use and file upload
file_tab, manual_tab  = st.tabs(["File mode", "Manual mode"])

# Configuration for file upload mode
with file_tab:
    
    st.markdown("")
    
    csv = st.file_uploader(
        label="Upload a CSV or excel file",
        type=["csv", "xlsx", "xls"]
    )

    

# Structure for manual inputs
with manual_tab:

    st.caption("###### _note: if you've uploaded a file to the file mode tab, please remove it before using manual mode, this mode is only for single inputs._")
    st.markdown("")

    # Manual inputs are controlled on the sidebar for better visualization
    with st.sidebar:

        # Logo
        st.image("logo.jpeg", use_column_width=True)

        # Title
        st.markdown("## Manual inputs for manual mode")
        st.caption("Please, fill the inputs below to get a prediction (prediction changes after each input)")
        
        # Model inputs avaliable on the selectboxes
        # Numerical inputs dealt with manual numeric inputs or + and - buttons
        # Binary variables dealt with selectboxes
        bank_months_count = st.number_input(label="Bank months count", 
                                            min_value=0, 
                                            step=1, 
                                            max_value=1200, 
                                            value=0
                                            )
        
        credit_risk_score = st.number_input(label="Credit risk score", 
                                            min_value=-1000, 
                                            step=1, 
                                            max_value=1000, 
                                            value=1
                                            )
        
        customer_age = st.number_input(label="Customer age", 
                                       min_value=1, 
                                       step=1, 
                                       max_value=100, 
                                       value=18
                                       )
        
        date_of_birth_distinct_emails_4w = st.number_input(
            label="Date of birth distinct emails 4w",
            value=0,
            min_value=0,
            step=1
        )

        device_distinct_emails_8w = st.number_input(label="Device distinct emails 8w", 
                                                    min_value=0, 
                                                    step=1, 
                                                    max_value=10, 
                                                    value=0
                                                    )
        
        device_os = st.selectbox(
            label="Device OS",
            options=['windows', 'other', 'linux', 'macintosh', 'x11'],
            index=2
        )

        email_is_free = st.selectbox(label="Email is free", 
                                     options=["Yes", "No"], 
                                     index=0
                                     )

        employment_status = st.selectbox(
            label="Employment Status",
            options=['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG'],
            index=0
        )

        foreign_request = st.selectbox(label="Foreign request", 
                                       options=["Yes", "No"], 
                                       index=0
                                       )
        
        housing_status = st.selectbox(
            label="Housing Status",
            options=['BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG'],
            index=0
        )

        has_other_cards = st.selectbox(label="Has other cards", 
                                        options=["Yes", "No"], 
                                        index=0
                                          )
        
        income = st.number_input(label="Income", 
                                 min_value=0.0, 
                                 step=0.1, 
                                 max_value=1.0, 
                                 value=0.1
                                 )
        
        keep_alive_session = st.selectbox(label="Keep alive session", 
                                          options=["Yes", "No"], 
                                          index=0
                                          )
        
        month = st.number_input(label="Month of request", 
                                min_value=0, 
                                step=1, 
                                max_value=7, 
                                value=1
                                )
        
        name_email_similarity = st.number_input(label="Email name similarity", 
                                                min_value=0.0, 
                                                step=0.01, 
                                                max_value=1.0, 
                                                value=0.0
                                                )
        
        payment_type = st.selectbox(
            label="Payment type",
            options=['AA', 'AB', 'AC', 'AD', 'AE'],
            index=0
        )

        phone_home_valid = st.selectbox(label="Phone home valid", 
                                        options=["Yes", "No"], 
                                        index=0
                                        )

        prev_address_months_count = st.number_input(label="Previous address months count", 
                                                    min_value=0, 
                                                    step=1, 
                                                    max_value=1000, 
                                                    value=0
                                                    )
        
        proposed_credit_limit = st.number_input(label="Proposed credit limit", 
                                                min_value=0, 
                                                step=1, 
                                                max_value=1000000, 
                                                value=1
                                                )
        
        source = st.selectbox(
            label="Source",
            options=['INTERNET', 'TELEAPP'],
            index=0
        )
        
        zip_count_4w = st.number_input(label="Zip count 4w", 
                                       min_value=1, 
                                       step=1, 
                                       max_value=10000, 
                                       value=1
                                       )

    
        # Parse binary options to boolean for the model
        has_other_cards = has_other_cards == "Yes"
        phone_home_valid = phone_home_valid == "Yes"
        foreign_request = foreign_request == "Yes"
        keep_alive_session = keep_alive_session == "Yes"
        email_is_free = email_is_free == "Yes"

# Only request server if data changes to avoid unnecessary requests
@st.cache_data
def post(json: dict) -> requests.Response:
    
    # Post data to model server
    return requests.post(
        url=url,
        headers=headers,
        json=json
    )

# Structure for csv and excel files
if csv:

    try:
        uploaded_data_df = pd.read_csv(csv)
    except UnicodeDecodeError:
        uploaded_data_df = pd.read_excel(csv)
    
    with file_tab:
        st.dataframe(uploaded_data_df)

    # Convert to json for the request
    data = uploaded_data_df.to_dict(orient="records")
    response = post(json={"data": data})
    
    # Information for the user
    st.caption('<p style="color: grey; text-align: center;">This is a preview of the raw data you have uploaded. This data is processed before being sent to the model server.</p>', unsafe_allow_html=True)

# Structure for manual inputs
else:

    # Build the json from the manual inputs on frontend
    data = [{
            "device_os": device_os,
            "source": source,
            "housing_status": housing_status,
            "employment_status": employment_status,
            "payment_type": payment_type,
            "date_of_birth_distinct_emails_4w": date_of_birth_distinct_emails_4w,
            "name_email_similarity": name_email_similarity,
            "credit_risk_score": credit_risk_score,
            "customer_age": customer_age,
            "month": month,
            "has_other_cards": has_other_cards,
            "proposed_credit_limit": proposed_credit_limit,
            "prev_address_months_count": prev_address_months_count,
            "zip_count_4w": zip_count_4w,
            "income": income,
            "device_distinct_emails_8w": device_distinct_emails_8w,
            "bank_months_count": bank_months_count,
            "phone_home_valid": phone_home_valid,
            "foreign_request": foreign_request,
            "keep_alive_session": keep_alive_session,
            "email_is_free": email_is_free
        }]

    # Respond to the post request with the predictions
    response = post(json={"data": data})

# Threshold for fraud
st.markdown("### Threshold")
threshold = st.number_input(
    label="Please, set your threshold for fraud detection",
    min_value=0.0,
    max_value=1.0,
    step=0.05,
    value=0.0
)

# Danger zone for fraud
st.markdown("### Danger zone")
danger_zone = st.number_input(
    label="Please, set your danger zone for fraud detection (this is the gap between the threshold and the probability)",
    min_value=0.0,
    max_value=1.0,
    step=0.05,
    value=0.15
)

# Dataframe with the probabilities
probabilities = pd.DataFrame(response.json()["probability"])

# Classifications based on the threshold and danger zone
defaults = [
    "Potential fraud" if p > threshold 
    else "Normal" if p < threshold and (threshold - p) > danger_zone 
    else "Danger zone"
    for p in response.json()["probability"]
]

# Union of the probabilities and classifications
results = pd.DataFrame({
    "Probability": probabilities[0],
    "Result": defaults
})

# Mark in red if fraud, in green if normal or in orange if its inside the danger zone
results_styled = results.style.applymap(highlight_fraud, subset=['Result'])

# Show results in a table
st.markdown("### Predictions")
st.table(results_styled)

# Disclaimer
st.caption('<p style="color: grey; text-align: center;">DISCLAIMER: This app is for educational purposes only; it is not intended to be used in production.</p>', unsafe_allow_html=True)
