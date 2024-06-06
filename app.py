import streamlit as st
import time
import pickle

st.title("Twitter Sentiment Analysis")

# Load the pretrained model
with open('xgb_bow.pkl', 'rb') as f:
    model = pickle.load(f)

tweet = st.text_input('Enter Tweet')
submit = st.button('Predict')

if submit:
    

    start = time.time()

    # Predict sentiment
    predictions = model.predict([tweet])

    # Get class with maximum probability
    prediction = predictions[0].argmax()

    end = time.time()

    st.write('Analysis time taken:', round(end-start, 2), 'seconds')

    st.write("Sentiment Predicted:", prediction)
    