# ai_model.py
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import accuracy_score

# 1. Load the "20 Newsgroups" dataset from sklearn
data = datasets.fetch_20newsgroups(subset='all', categories=['sci.med', 'rec.sport.baseball'])

# 2. Prepare the data (X for the text, y for the labels)
X = data.data  # List of text data
y = data.target  # List of target labels

# 3. Split the data into training and testing sets (75% training, 25% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. Vectorize the text data (convert text to numerical features)
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# 5. Build the Naive Bayes model
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# 6. Evaluate the model on the test data
y_pred = clf.predict(X_test_counts)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# 7. Save the trained model and the vectorizer to pickle files
with open('model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)
