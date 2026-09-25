import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
import pickle


st.title('Passenger Survival Probability - Using Deep Learning')


pclass = st.slider(
    'Enter the passenger class',
    1,
    3
)

sex = st.selectbox(
    'Select Passenger Gender',
    ['male', 'female']
)

sibsp = st.slider(
    'Enter the passenger total number of siblings and spouse',
    0,
    10
)

parch = st.slider(
    'Enter the passenger total number of parents and children',
    0,
    8
)

fare = st.number_input(
    'Enter the Fare of passenger'
)

embarked = st.selectbox(
    'Enter Passenger Boarding Station',
    ['Southampton', 'Chebourg', 'Queenstown']
)


# Create user DataFrame
user = pd.DataFrame([
    {
        'Pclass': pclass,
        'Sex': sex,
        'SibSp': sibsp,
        'Parch': parch,
        'Fare': fare,
        'Embarked': embarked
    }
])


# Load trained model
trained_model = load_model('model.h5')


# Load Label Encoder
with open('lable_encoder.pkl', 'rb') as file:
    label = pickle.load(file)


# Load One Hot Encoder
with open('one_hot_encoder.pkl', 'rb') as file:
    one_hot = pickle.load(file)


# Load Scaler
with open('scale.pkl', 'rb') as file:
    scaler = pickle.load(file)


# -------------------------------
# Encoding
# -------------------------------

# Encode Sex
user['Sex'] = label.transform(user['Sex'])


# Encode Embarked
embarked_encoded = one_hot.transform(
    user[['Embarked']]
)

embarked_encoded = pd.DataFrame(
    embarked_encoded,
    columns=one_hot.get_feature_names_out()
)


# Remove original Embarked and add encoded columns
user = pd.concat(
    [
        user.drop(columns=['Embarked']),
        embarked_encoded
    ],
    axis=1
)


# -------------------------------
# Scaling
# -------------------------------

num_cols = ['Pclass', 'SibSp', 'Parch', 'Fare']

user[num_cols] = scaler.transform(user[num_cols])

# Prediction

if st.button('Predict Survival Probability'):

    y = trained_model.predict(user)[0][0]

    st.write("Survival Probability:", y)

    if y > 0.5:
        st.success('Higher chance to survive')
    else:
        st.error('Less chance to survive')