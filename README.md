# SMS Spam Detection System

## Overview
SMS Spam Detection System is a machine learning model that takes an SMS as input and predicts whether it is a spam message or not. The model is built using Python and deployed on the web using Streamlit. This project was developed as a part of AICTE Internship on AI: Transformative Learning with TechSaksham – A joint CSR initiative of Microsoft & SAP, focusing on AI Technologies, where I worked extensively on applying machine learning techniques to solve real-world problems.

## Technology Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit

## Features
- Data collection
- Data cleaning and preprocessing
- Exploratory Data Analysis
- Model building and selection
- Web deployment using Streamlit

### Data Collection
The dataset used for this project is the SMS Spam Collection Dataset, sourced from Kaggle. It consists of over 5,500 SMS messages, each labeled as either spam or not spam. You can find the dataset [here](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).

### Data Cleaning and Preprocessing
The dataset was cleaned by removing null values and duplicates, and the "type" column was label-encoded. The preprocessing steps involved tokenizing the messages, removing special characters, punctuation, and stop words, and applying stemming. In addition, all text was converted to lowercase for uniformity.

### Exploratory Data Analysis
Exploratory Data Analysis (EDA) was performed to better understand the dataset. Metrics like character count, word count, and sentence count were calculated for each message. Visualizations such as bar charts, pie charts, heatmaps, and word clouds were used to identify patterns, including frequently occurring words in spam and non-spam messages.

### Model Building and Selection
Various classifiers were tested, including Naive Bayes, Random Forest, K-Nearest Neighbors (KNN), Decision Tree, Logistic Regression, ExtraTreesClassifier, and Support Vector Classifier (SVC). The model achieving the highest precision was selected for deployment.

### Web Deployment
The model was deployed on the web using Streamlit. The user interface has a simple input box where the user can input a message, and the model will predict whether it is spam or not spam.

## Demo
To try out the SMS Spam Detection model, visit [here](https://sms-spam-detection-system.streamlit.app/).

## Usage
To use the SMS Spam Detection model on your own machine, follow these steps:

+ Clone this repository.
+ Install the required Python packages using 
```
pip install -r requirements.txt
```
+ Run the model using 
```
streamlit run app.py
```
+ Visit localhost:8501 on your web browser to access the web app.

## Contributions
Contributions to this project are welcome. If you find any issues or have any suggestions for improvement, please open an issue or a pull request on this repository.
