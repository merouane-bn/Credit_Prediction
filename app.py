import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model from the pickle file
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # Get input from the form
    credit_history = float(request.form['Credit_History'])
    married = int(request.form['Married'])  # Ensure this is numerical if your model expects it
    coapplicant_income = float(request.form['CoapplicantIncome'])

    # Create a feature array based on model requirements
    final_features = np.array([[credit_history, married, coapplicant_income]])
    
    # Make prediction
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='La réponse à votre crédit est: {}'.format(output))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # Expose to all interfaces
