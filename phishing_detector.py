import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Loading dataset...")

# Load dataset
data = pd.read_csv("Phishing_Email.csv")

# Remove empty rows
data = data.dropna()

# Features and labels
X = data["Email Text"]
y = data["Email Type"]

# Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
print("\nAccuracy:")
print(f"{accuracy_score(y_test, predictions) * 100:.2f}%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\n==============================")
print("PHISHING EMAIL DETECTOR READY")
print("==============================")

# Email testing loop
while True:

    email = input("\nEnter email text (or type exit):\n")

    if email.lower() == "exit":
        print("Program Closed.")
        break

    email_vector = vectorizer.transform([email])

    prediction = model.predict(email_vector)

    print("\nPrediction:", prediction[0])