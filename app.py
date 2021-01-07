# Import flask for web applications.
import flask as fl

# Numpy for numerical arrays.
import numpy as np

# pickle for saving and restoring ML models.
import joblib

# For restoring a keras model.
from tensorflow.keras.models import load_model
# wind value to test models in this file.
t = 10
# Import my polnomial regression model-in same dir
polyreg = joblib.load("models/poly-reg.pkl")
# Need poly features to make a prediction for [[x, x^2, x^3]]
print(polyreg.predict([[t, t ** 2, t ** 3]]), "for t= ", t) # shape ok but not doing polynomial features
########## Create a new web application ##########

app = fl.Flask(__name__, static_url_path='', static_folder='static')

########## Add root app ##########
@app.route('/')
def home():
     # Access static content over the pre-configured /static/
     return app.send_static_file('index.html')

	 

########## Tell flask to make model 1 available at /model1 ##########
# model 1 is polynomial regression
# file: poly-reg.pkl

@app.route('/api/model1/<int:w>')
# curl test at 127.0.0.1:5000/api/model1/10 ok

def model1(w):
    # Make the prediction using our model with w, w^2, w^3.
    p = polyreg.predict([[w, w ** 2, w ** 3]])
    return {"value": str(p[0])} # Object must be a string.



# model 2 is a sequential neural network
# file: neural-nw.h5
# How to get the data into this function? Via the url, goes with request.
# Commenting  out as errors on PA for model2
# Import my neural network model.
model = load_model("Models/neural-network.h5")
# Test make a prediction - ok
print(model.predict([[t]]), "for t= ", t) 
@app.route('/api/model2/<int:w>')
def model2(w):
    p = model.predict([[w]]) # TypeError: Object of type ndarray is not JSON serializable if try to return this
    return {"value": str(p[0][0])} # Object must be a string  
	
# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()} # Return uniform numbers from 0 to 1. 

# Add normal route.
@app.route('/api/normal') # gen random numbers centred around 0 minus or positive.
def normal(): 
  return {"value": np.random.normal()} # Return Numpy random normal number from Python Dictionary.

if __name__ == '__main__':
    app.run(debug= True)	