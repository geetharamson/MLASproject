#!flask/bin/python
from flask import Flask
import tensorflow.keras as kr
from tensorflow.keras.models import load_model
import json

model = load_model('Models/wind_power')
#print(model.summary())
print(model.predict([1.5]))
print(model.predict([1.5]).tolist())



app = Flask(__name__,static_url_path='', static_folder='static')

@app.route('/')

@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/predict/<int:x>', methods=['GET'])
@app.route('/predict/<float:x>', methods=['GET'])
def predictor(x):
    prediction = model.predict([x])
    print(prediction[0][0])

    return str(prediction[0][0])



if __name__ == '__main__':
    app.run(debug= True)