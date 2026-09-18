Book Recommendation System

Dataset: Books Dataset for NLP and Recommendation Systems
Source: Kaggle
Kaggle Link:
https://www.kaggle.com/datasets/sinatavakoli/books-dataset-for-nlp-and-recommendation-systems

The dataset contains book information such as title, author, ratings,
description, and image URL.

Project Structure

├── book.csv
├── task.ipynb
├── app.py
├── requirements.txt
├── .gitignore
├── books.pickle
├── tfidf_matrix.joblib
├── tfidf.joblib
└── README.md

Required Python Packages

Create requirements.txt with:

streamlit
pandas
scikit-learn
nltk
joblib

Install:
pip install -r requirements.txt

Run:
streamlit run app.py

Deployed App:
https://book-recommendation-system-ic8z.onrender.com/
