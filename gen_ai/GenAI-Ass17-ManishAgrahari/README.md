# Assignment 17 — Text Cleaning, Preprocessing & NLP Pipeline

This assignment implements a complete NLP text preprocessing pipeline using Python, Pandas, Regex, and NLTK.

## Dataset

A custom dataset containing 30 text samples was created with common text issues such as:
- Uppercase/lowercase variations
- Punctuation and numbers
- Extra spaces
- URLs and emails
- HTML tags
- Emojis and special characters
- Repeated characters
- Slang

## Requirements

Python 3.x

Install required libraries:

```bash
pip install pandas nltk

import nltk

## if required
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')