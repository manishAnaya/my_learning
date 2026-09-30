import streamlit as st
from keras.models import load_model
import pickle
from keras.utils import pad_sequences
import numpy as np

model = load_model('rrn_model.h5')

with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

st.title('Twitter Tweet Sentiment Analysis')

tweet = st.text_area('Please Tweets: ')

if st.button('Predict Sentiment') and tweet.strip():
    sequences = tokenizer.texts_to_sequences([tweet])
    sequences = pad_sequences(sequences, padding='post', maxlen=166)

    prediction = model.predict(sequences)
    predicted_class = np.argmax(prediction, axis=1)[0]

    sentiment_map = {
        0: 'Negative',
        1: 'Neutral',
        2: 'Positive',
    }

    st.write('predicted Sentiment:', sentiment_map[predicted_class])