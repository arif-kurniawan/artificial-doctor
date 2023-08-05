# Artificial Doctor
#### Quickly Find Out Your Disease

Artificial Doctor is an artificial intelligence-based web application that can predict diseases based on the symptoms felt by the user. However, this application does not guarantee that the prediction results are always correct, therefore you should still consult a doctor. This application only helps for early detection of possible diseases.

In making machine learning models, a dataset containing symptoms and diseases is used, as well as the weight of the influence of each symptom of the disease. After going through the training process with the Random Forest classification method, a model is generated that is stored in a file that is loaded in this application.

## Features
- Input name and sex
- User can choose more than one symptom
- The output is a type of disease based on the selected symptoms

## Tech

Artificial Doctor uses some open source softwares and projects:

- [Python] - Powerful and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.
- [Flask] - The web application framework is a micro framework written in the Python programming language and using the dependencies of Werkzeug and Jinja2
- [Bootstrap] - Powerful, extensible, and feature-packed frontend toolkit.
- [jQuery] - Fast, small, and feature-rich JavaScript library.

## Installation

Artificial Doctor requires [Python](https://python.org/) 3.10 and Flask to run.
Install some python library needed by this application:
#### Flask
```sh
pip install flask
```
#### Pandas
Library for data exploration
```sh
pip install pandas
```
#### Sklearn
Library for machine learning
```sh
pip install scikit-learn
```

## How to run
Extract this application to your directory.
Change your prompt to application directory and set you flask app to environment variable, using this command (Linux) :
```sh
set FLASK_APP=app.py
```
app.py is the file name of flask application.

Run application server from your python virtual environment
```sh
flask run
```
If you want to run in public server you can add argument like this example
```sh
flask run --host=100.101.102.34 --port:5000
```
100.101.102.34 is example of public IP address

## Demonstration
Open this youtube video :
https://www.youtube.com/watch?v=i1K1ggaVRIE

[Python]: <https://www.python.org/>
[FLask]: <https://flask.palletsprojects.com/>
[Bootstrap]: <https://getbootstrap.com/>
[jQuery]: <https://jquery.com/>