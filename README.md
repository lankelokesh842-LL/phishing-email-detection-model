# Phishing Email Detection Model

## Overview

This project is a Machine Learning-based phishing email detection system that classifies emails as either **Phishing Email** or **Safe Email**. The model is trained using a phishing email dataset and uses Natural Language Processing (NLP) techniques for feature extraction.

## Features

* Email text analysis
* TF-IDF feature extraction
* Machine Learning classification using Naive Bayes
* Accuracy measurement
* Confusion Matrix generation
* Classification Report
* Real-time email prediction

## Technologies Used

* Python
* Pandas
* Scikit-learn
* NumPy
* TF-IDF Vectorizer
* Multinomial Naive Bayes

## Dataset

Phishing Email Dataset from Kaggle.

## Results

* Accuracy: 91.49%
* Successfully classifies emails as Phishing or Safe.

## How to Run

### Install Dependencies

```bash
python -m pip install pandas scikit-learn numpy matplotlib seaborn
```

### Run the Project

```bash
python phishing_detector.py
```

### Test an Email

Enter any email content when prompted and the model will predict whether it is a Phishing Email or Safe Email.

## Sample Output

* Accuracy Score
* Confusion Matrix
* Classification Report
* Email Classification Prediction
Dataset used:
https://www.kaggle.com/datasets/xxxxx/phishing-email-dataset
