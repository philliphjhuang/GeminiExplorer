import streamlit as st
from google.auth import default
from google.cloud import storage

# Authenticate using Application Default Credentials (ADC)
credentials, project_id = default()

# Create a client using the authenticated credentials
client = storage.Client(credentials=credentials, project=project_id)

# Test the authentication by listing buckets
try:
    buckets = list(client.list_buckets())
    st.write("Authentication successful! Buckets:")
    for bucket in buckets:
        st.write(bucket.name)
except Exception as e:
    st.error(f"Authentication failed: {e}")