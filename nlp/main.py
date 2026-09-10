import streamlit as st
import pickle
import joblib
import pandas as pd
import sklearn
import nltk

st.title('Movie Recommendation System')

with open('movies.pickle', 'rb') as file:
    movies = pickle.load(file)

movie_name = movies.title.values

selected_movie = st.selectbox('Please Select Movie', movie_name)

similarities = joblib.load('similarity.joblib')

def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    recommendation = similarities[movie_index]
    movie_list = sorted(enumerate(recommendation), reverse=True, key=lambda x: x[1])[1: 6]
    print(movie_list)
    recommended_movies = []
    for item in movie_list:
        recommended_movies.append(movies.title[item[0]])
    print(recommended_movies)
    return recommended_movies

if st.button('Recommend'):
    st.write("Recommended movies as per movie are:")
    m = recommend(selected_movie)
    for i in m:
        st.write(i)
    