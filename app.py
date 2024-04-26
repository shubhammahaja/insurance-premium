import numpy as np
import pickle
import math
from flask import Flask, request, jsonify, render_template

app = Flask(__name__,template_folder= "template", static_folder= "staticfiles") ## assign Flask = app
model = pickle.load(open('build.pkl','rb'))   ### import model

@app.route('/')
def home():
    return render_template('index.html')  # read index.html file

@app.route('/predict', methods=['POST'])   ###transfer data from html to python / server

def predict():
    int_features= [float(x)  for x in request.form.values()]   # request for data values
    final_features= [np.array(int_features)]  # convert into array
    prediction = model.predict(final_features)  # Predict
    output = round(prediction[0]**2,4)
    return render_template('index.html',prediction_text="Premium Amount {}".format(math.floor(output)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)