import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title('🫁 Lung Cancer Diagnosis')
st.write("Please fill out the following information to assess the likelihood of lung cancer.")
