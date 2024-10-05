# app.py
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the saved model and vectorizer from the pickle files
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def index():
    # Render the main page with a form for inputting text
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the message input from the form
        message = request.form['message']
        data = [message]
        
        # Vectorize the input message
        vect = vectorizer.transform(data).toarray()
        
        # Make a prediction using the loaded model
        prediction = model.predict(vect)
        
        # Render the result page with the prediction
        if prediction == 1:
            result = "This is Spam"
        else:
            result = "This is Not Spam"
        
        return render_template('result.html', prediction=result)

if __name__ == '__main__':
    # Start the Flask server in debug mode
    app.run(debug=True)
