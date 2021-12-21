from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pickle
import numpy as np
import json
import pandas as pd
import glob
import os.path

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)



# # making a class for a particular resource
# # the get, post methods correspond to get and post requests
# # they are automatically mapped by flask_restful.


class Predict(Resource):
    def post(self):
        '''
        This function takes the following inputs:
        1) model_name - pickle file to be used as model input
        2) config_name - config csv file format for loading the configurations
        3) model inputs - variable name (parameter) along with parameter value
        
        Post reading the inputs - model file is utilized to forecast the output.
        '''

        model_name = request.form.get("model")
        config_name = request.form.get("config")
        input_format = request.form.get("input_format")
        
        model_filename = model_name + ".pkl"
        config_filename = config_name + ".csv"
   
        #Loading Models
        #model = pickle.load(open('source_model/' + model_filename , 'rb'))
        model = joblib.load('source_model/' + model_filename )

        #loading configrations
        config = pd.read_csv('source_config/' + config_filename)
        
        print(config)
        print(model)

        if input_format == 'value' :
            #Definition
            dict={}    
            for i in range(len(config)):
                dict["var{0}".format(i+1)] = float(request.form.get(config.iloc[i,0]))
                
            values = dict.values()
            values_list = list(values)
            print(values_list)
            prediction = model.predict([values_list])

        elif input_format == 'file' :
            data = request.files["file"]
            data = pd.read_csv(data)

            prediction = model.predict(data)



        return jsonify(prediction.tolist())





api.add_resource(Predict, '/predict')

# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=False)
