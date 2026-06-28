# NLP Text Preprocessing Pipeline

## Overview

This project demonstrates the basic Natural Language Processing (NLP) preprocessing pipeline using Python and NLTK.

The program takes a text paragraph as input and performs multiple NLP operations to prepare the text for further analysis and machine learning tasks.

---

## Features

* Sentence Tokenization
* Word Tokenization
* Stop Word Removal
* Part-of-Speech (POS) Tagging
* Lemmatization
* Named Entity Recognition (NER)

---

## Technologies Used

* Python
* NLTK (Natural Language Toolkit)

---

## NLP Pipeline

```text
Input Text
     ↓
Sentence Tokenization
     ↓
Word Tokenization
     ↓
Stop Word Removal
     ↓
POS Tagging
     ↓
Lemmatization
     ↓
Named Entity Recognition (NER)
     ↓
Processed Output
```

---

## Project Structure

```text
NLP-Text-Preprocessing-Pipeline/
│
├── practice.py
├── README.md
└── requirements.txt
```

---

## Sample Input

```text
John works at Google in Bengaluru. Sarah visited Microsoft in Delhi.
```

---

## Sample Operations

### Sentence Tokenization

```text
[
 'John works at Google in Bengaluru.',
 'Sarah visited Microsoft in Delhi.'
]
```

### Word Tokenization

```text
['John', 'works', 'at', 'Google', 'in', 'Bengaluru', '.']
```

### Stop Word Removal

```text
['John', 'works', 'Google', 'Bengaluru']
```

### Lemmatization

```text
work
visit
```

### Named Entity Recognition

```text
John       → PERSON
Google     → ORGANIZATION
Bengaluru  → LOCATION
Sarah      → PERSON
Microsoft  → ORGANIZATION
Delhi      → LOCATION
```

---




---

## Required NLTK Resources

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

---

## Learning Outcomes

Through this project, I learned:

* Text preprocessing techniques
* Tokenization methods
* Stop word removal
* POS tagging concepts
* Lemmatization using WordNet
* Named Entity Recognition (NER)
* Building an end-to-end NLP preprocessing pipeline

---

## Future Improvements

* Bag of Words (BoW)
* TF-IDF Vectorization
* Sentiment Analysis
* Text Classification
* NLP Web Application using Streamlit

---

## Author

Ramya S

Aspiring AI & Machine Learning Engineer | Exploring NLP, Machine Learning, and Data Science.

```
```
