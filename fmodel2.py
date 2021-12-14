from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pickle
import numpy as np
import json
import pandas as pd
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

#Loading Models
model = pickle.load(open('model/model.pkl', 'rb'))

#loading configrations
config=pd.read_csv('config/config.csv')


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.


class Predict(Resource):
    def post(self):
        #Definition
        dict={}
    
        for i in range(len(config)):
            #param = config.iloc[i,0]
            #dict["var{0}".format(i+1)] = request.args.get(param)
            dict["var{0}".format(i+1)] = request.args.get(config.iloc[i,0])
            
        values = dict.values()
        values_list = list(values)

        prediction = model.predict([values_list])
        return jsonify(prediction.tolist())



api.add_resource(Predict, '/predict')

# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug = False)

