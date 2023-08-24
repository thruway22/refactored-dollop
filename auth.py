import json
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

class Connect:
    def __init__(self):
        self.key = st.secrets['textkey']
        self.credentials = service_account.Credentials.from_service_account_info(json.loads(self.key))
        self.client = firestore.Client(credentials=self.credentials, project='my-family-fund')

    def get_collection(self, collection):
        return self.client.collection(collection)