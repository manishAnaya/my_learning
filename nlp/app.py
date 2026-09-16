import streamlit as st
import pickle
import joblib

st.title('Movies Recommendation System')

with open('movies.pickle', 'rb') as file:
    movies = pickle.load(file)

movie_list = movies.title.values

selected_movie = st.selectbox('Please Select Movie', movie_list)

similarity = joblib.load('similarity.joblib')

def recommend(selected):
    movie_index = movies[movies.title == selected].index[0]
    recommendation = similarity[movie_index]
    list = sorted(enumerate(recommendation), reverse=True, key=lambda x: x[1])[1:6]
    recom_movie = []
    for item in list:
        recom_movie.append(movies.title[item[0]])
    return recom_movie

if st.button('Recommend'):
    st.write("Recommended movies as per movie are:")
    m = recommend(selected_movie)
    for i in m:
        st.write(i)