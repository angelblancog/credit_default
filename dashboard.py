import requests
import streamlit as st
import os

HOST = os.environ["MODEL_SERVER_HOST"]
PORT = os.environ["MODEL_SERVER_PORT"]
ENDPOINT = os.environ["MODEL_SERVER_ENDPOINT"]

url = f"{HOST}:{PORT}{ENDPOINT}"

headers = {
    "Content-Type": "application/json",
}

st.title("Credit Card Default Predictor")
st.markdown("This app predicts the **Default** probability of a credit card user")

manual_tab, file_tab = st.tabs(["Manual mode", "File mode"])

with manual_tab:

    with st.sidebar:
        # Model inputs
        device_os = st.selectbox(
            label="Device OS",
            options=['windows', 'other', 'linux', 'macintosh', 'x11'],
            index=2
        )

        employment_status = st.selectbox(
            label="Employment Status",
            options=['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG'],
            index=0
        )

        housing_status = st.selectbox(
            label="Housing Status",
            options=['BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG'],
            index=0
        )

        source = st.selectbox(
            label="Source",
            options=['INTERNET', 'TELEAPP'],
            index=0
        )

        payment_type = st.selectbox(
            label="Payment type",
            options=['AA', 'AB', 'AC', 'AD', 'AE'],
            index=0
        )

        date_of_birth_distinct_emails_4w = st.number_input(
            label="Date of birth distinct emails 4w",
            value=0,
            min_value=0,
            step=1
        )


        name_email_similarity = st.number_input(label="name_email_similarity", min_value=0, step=1, max_value=1000, value=1)
        credit_risk_score = st.number_input(label="credit_risk_score", min_value=0, step=1, max_value=1000, value=1)
        customer_age = st.number_input(label="customer_age", min_value=0, step=1, max_value=1000, value=1)
        month = st.number_input(label="month", min_value=0, step=1, max_value=1000, value=1)
        has_other_cards = st.number_input(label="has_other_cards", min_value=0, step=1, max_value=1000, value=1)
        proposed_credit_limit = st.number_input(label="proposed_credit_limit", min_value=0, step=1, max_value=1000, value=1)
        prev_address_months_count = st.number_input(label="prev_address_months_count", min_value=0, step=1, max_value=1000, value=1)
        zip_count_4w = st.number_input(label="zip_count_4w", min_value=0, step=1, max_value=1000, value=1)
        income = st.number_input(label="income", min_value=0, step=1, max_value=1000, value=1)
        device_distinct_emails_8w = st.number_input(label="device_distinct_emails_8w", min_value=0, step=1, max_value=1000, value=1)
        bank_months_count = st.number_input(label="bank_months_count", min_value=0, step=1, max_value=1000, value=1)
        phone_home_valid = st.number_input(label="phone_home_valid", min_value=0, step=1, max_value=1000, value=1)
        
        foreign_request = st.selectbox(label="foreign_request", options=["Yes", "No"], index=0)
        keep_alive_session = st.selectbox(label="keep_alive_session", options=["Yes", "No"], index=0)
        email_is_free = st.selectbox(label="email_is_free", options=["Yes", "No"], index=0)
        
        # Parse to boolean
        foreign_request = foreign_request == "Yes"
        keep_alive_session = keep_alive_session == "Yes"
        email_is_free = email_is_free == "Yes"

with file_tab:
    st.file_uploader(
        label="Upload a CSV file",
        type=["csv"]
    )


data = {
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
}

# Post data to model server
response = requests.post(
    url=url,
    headers=headers,
    json=data
)

st.markdown("### Response")
st.json(response.json())

status = response.json()['status']
give_credit = status == "Paid"

st.markdown(f"Status: {status}")
st.markdown(f"Give credit: {give_credit}")