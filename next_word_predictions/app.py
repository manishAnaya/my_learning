import streamlit as st
import pickle
from keras.models import load_model
from keras.utils import pad_sequences
import numpy as np

st.title('Next Word Predictions')

model = load_model('nextword_model.h5')

with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

reverse_index = {idx: word for word, idx in tokenizer.word_index.items()}

max_len = 44

def generate_text(seed_text, num_words=10):
    text = seed_text
    for _ in range(num_words):
        seq = tokenizer.texts_to_sequences([text])[0]
        padded = pad_sequences([seq], maxlen=max_len, padding='pre')
        predictions = model.predict(padded, verbose=0)
        pos = np.argmax(predictions)
        next_word = reverse_index.get(pos, ' ')
        text += ' '+next_word
    return text

seed = st.text_input('Enter starting text', 'Hello')

num_words = st.slider('Number of words to be predicted', 1, 20, 10)

if st.button('Generate'):
    result = generate_text(seed, num_words)
    st.write(result)