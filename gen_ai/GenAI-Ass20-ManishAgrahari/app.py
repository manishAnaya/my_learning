import streamlit as st
import pickle
import joblib
from sklearn.metrics.pairwise import cosine_similarity

st.title("Book Recommendation System")

st.write(
    "Find books similar to your selected book "
    "using content-based recommendation."
)

# Load books
with open("books.pickle", "rb") as file:
    books = pickle.load(file)

book_name = books.title.values

selected_book = st.selectbox('Please select a book', book_name)

# Load TF-IDF vectorizer
tfidf = joblib.load("tfidf.joblib")

# Load TF-IDF matrix
tfidf_matrix = joblib.load("tfidf_matrix.joblib")

def recommend_book(title):
    book_index = books[books.title == title].index[0]
    book_vector = tfidf_matrix[book_index]
    similarity = cosine_similarity(book_vector, tfidf_matrix).flatten()
    book_list = sorted(enumerate(similarity), reverse=True, key=lambda x: x[1])[1:6]
    recommended_books = []
    for book in book_list:
        recommended_books.append(books.title[book[0]])
    return recommended_books

if st.button('Recommend'):
    st.write("Recommended books are: ")
    recommendations = recommend_book(selected_book)
    for book in recommendations:
        st.write(book)