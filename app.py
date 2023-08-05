# import picke for reading machine learning model file
import pickle
# import pandas for creating dataframe
import pandas as pd

# import for flask and helpers
from flask import Flask, render_template, request
from helpers import apology

# Configure application
app = Flask(__name__)

# Load and open machine learning model file
model_file = open('model/model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

# Route for index/root
@app.route("/")
def index():
    return render_template("index.html")

# Route for predict page
@app.route("/predict", methods=["GET", "POST"])
def predict():
    """Predict"""
    if request.method == "GET":
        return render_template("predict.html")
    else:
        # Get input from text field and select
        name = request.form.get("name")
        sex = request.form.get("sex")
        symptoms = request.form.getlist("symptoms")
        # Set the greet
        greet = ""
        if sex == "M":
            greet = "Mr. "
        else:
            greet = "Mrs. "
        # Check, must input name
        if not name:
            return apology("Must give name")
        # Must select at least one symptom
        if len(symptoms) == 0:
            return apology("Must select at least one symptom")
        # Max can select 17 symptoms
        if len(symptoms) > 17:
            return apology("Max 17 symptoms that can be selected")
        print(symptoms)
        # create list of symptoms using format 17 columns
        data=[]
        for i in range(17):
            if i < len(symptoms):
                data.append(symptoms[i])
            else:
                data.append(0)
        print(data)

        # Convert list to dataframe
        df = pd.DataFrame([data], columns=['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4', 'Symptom_5',
                                           'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9', 'Symptom_10',
                                           'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14', 'Symptom_15',
                                           'Symptom_16', 'Symptom_17'])
        # Create prediction from ML model
        prediction = model.predict(df)

        # Get result of prediction
        output = prediction[0]

        # Dislay result
        return render_template('predicted.html', greet=greet, name=name, result=output)

# Route for about page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")