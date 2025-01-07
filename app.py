import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

import streamlit as st
import pickle 
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tk = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))


# Apply custom CSS
st.markdown("""
    <style>
    /* Set the background color for the main app container */
    [data-testid="stAppViewContainer"] {
        background-color: #E6E6FA;
        font-family: 'Arial', sans-serif;
        color: #333333;
    }
    /* Style the title */
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #4a4a4a;
        margin-bottom: 10px;
    }
    /* Style the subtitle */
    .subtitle {
        font-size: 20px;
        font-style: italic;
        text-align: center;
        color: #6c757d;
        margin-bottom: 20px;
    }
    /* Style input box */
    input[type="text"] {
        padding: 10px;
        font-size: 16px;
        border: 2px solid #ccc;
        border-radius: 5px;
    }
    /* Style buttons */
    div.stButton > button {
        background-color: #007bff; /* Button background color */
        color: #ffffff; /* Font color */
        font-size: 16px;
        border: 2px solid #0056b3; /* Border color */
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #0056b3; /* Background color on hover */
        border-color: #003f7f; /* Border color on hover */
        color: #e6e6e6; /* Font color on hover */
    }         
    /* Result display */
    .result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        border-radius: 5px;
        color: white;
    }
    .result-spam {
        background-color: #ff4d4d;
    }
    .result-not-spam {
        background-color: #28a745;
    }
    </style>
""", unsafe_allow_html=True)


# App layout
st.markdown('<div class="title">SMS Spam Detection Model</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Made by Hetvi Dalal</div>', unsafe_allow_html=True)


# User Input   
input_sms = st.text_input("Enter the SMS", help="Type your SMS message here")


if st.button('Predict', key="pulse"):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tk.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.markdown('<div class="result result-spam">Spam</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result result-not-spam">Not Spam</div>', unsafe_allow_html=True)