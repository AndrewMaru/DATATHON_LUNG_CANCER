import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('🫁 Lung Cancer Diagnosis')
st.write("Please fill out the following information to assess the likelihood of lung cancer.")

age = st.number_input('Age', min_value=1, max_value=120, value=30)
smoking = st.selectbox('Smoking', ['Yes', 'No'])
yellow_fingers = st.selectbox('Yellow Fingers', ['Yes', 'No'])
anxiety = st.selectbox('Anxiety', ['Yes', 'No'])
peer_pressure = st.selectbox('Peer Pressure', ['Yes', 'No'])
chronic_disease = st.selectbox('Chronic Disease', ['Yes', 'No'])
fatigue = st.selectbox('Fatigue', ['Yes', 'No'])
allergy = st.selectbox('Allergy', ['Yes', 'No'])
wheezing = st.selectbox('Wheezing', ['Yes', 'No'])
alcohol = st.selectbox('Alcohol Consuming', ['Yes', 'No'])
coughing = st.selectbox('Coughing', ['Yes', 'No'])
shortness_of_breath = st.selectbox('Shortness of Breath', ['Yes', 'No'])
swallowing_difficulty = st.selectbox('Swallowing Difficulty', ['Yes', 'No'])
chest_pain = st.selectbox('Chest Pain', ['Yes', 'No'])

# Convert inputs to numerical (assuming 1 = Yes, 0 = No)
def binary_encode(value):
    return 1 if value == 'Yes' else 0

data = pd.DataFrame([[
    age,
    binary_encode(smoking),
    binary_encode(yellow_fingers),
    binary_encode(anxiety),
    binary_encode(peer_pressure),
    binary_encode(chronic_disease),
    binary_encode(fatigue),
    binary_encode(allergy),
    binary_encode(wheezing),
    binary_encode(alcohol),
    binary_encode(coughing),
    binary_encode(shortness_of_breath),
    binary_encode(swallowing_difficulty),
    binary_encode(chest_pain)
]], columns=[
    'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE',
    'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING', 'ALCOHOL CONSUMING',
    'COUGHING', 'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN'
])

# Predict button
if st.button('Predict'):
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of lung cancer. Please consult a doctor.")
    else:
        st.success("✅ No Lung Cancer.")
