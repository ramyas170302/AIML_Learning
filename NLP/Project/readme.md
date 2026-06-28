# 📩 Spam Message Detector using NLP

## 📌 Project Overview

This project is a **Spam Message Detector** built using **Natural Language Processing (NLP)** and **Machine Learning**. It classifies a given message as either **Spam** or **Ham (Not Spam)**.

A user enters a message in the Streamlit web application, and the trained model predicts whether the message is spam or not.

---

## 🚀 Features

* Detects Spam and Ham messages
* User-friendly Streamlit interface
* NLP-based text preprocessing
* TF-IDF feature extraction
* Multinomial Naive Bayes classifier
* Displays prediction with confidence score

---

## 🛠️ Technologies Used

* Python
* Pandas
* NLTK
* Scikit-learn
* Streamlit
* Pickle

---

## 📂 Dataset

The project uses the **SMS Spam Collection Dataset**, which contains SMS messages labeled as:

* **Spam**
* **Ham**

---

## 📊 NLP Preprocessing Steps

The following preprocessing steps are applied to every message:

1. Convert text to lowercase
2. Word Tokenization
3. Remove Stop Words
4. POS Tagging
5. Lemmatization
6. Join words into a cleaned sentence

---

## 🤖 Machine Learning Pipeline

Message
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Multinomial Naive Bayes Model
↓
Spam / Ham Prediction

---

## 📁 Project Structure

```
Spam-Message-Detector/
│
├── app.py
├── train.py
├── spam.csv
├── model.pkl
├── tfidf.pkl
├── requirements.txt
└── README.md
```

---



## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 Example

### Input

```
Congratulations! You have won ₹1,00,000.
Click here to claim your prize.
```

### Output

```
🚨 Spam Message
```

---

### Input

```
Hi, are you coming to college today?
```

### Output

```
✅ Ham Message
```

---

## 📈 Model

Algorithm Used:

* Multinomial Naive Bayes

Feature Extraction:

* TF-IDF Vectorizer

---

## 📚 Skills Demonstrated

* Data Preprocessing
* Natural Language Processing
* Text Classification
* Machine Learning
* TF-IDF
* Naive Bayes
* Streamlit Deployment
* Model Serialization using Pickle

---

## 👩‍💻 Author

**Ramya**

Built as a learning project to understand the complete NLP workflow—from text preprocessing to machine learning model deployment using Streamlit.
