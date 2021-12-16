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

# All files ending with .pkl in source_model
# model_path = 'source_model\\*pkl'
# model_files = glob.glob(model_path)
# print(model_files)
# max_model_file = max(model_files, key=os.path.getctime)

# model_dst= 'model\\model.pkl'
# shutil.copy(max_model_file,model_dst)


# # All files ending with .csv in source_config
# config_path = 'source_config\\*csv'
# config_files = glob.glob(config_path)
# max_config_file = max(config_files, key=os.path.getctime)

# config_dst= 'config\\config.csv'
# shutil.copy(max_config_file,config_dst)






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

        model_name = request.args.get("model")
        config_name = request.args.get("config")
        
        model_filename = model_name + ".pkl"
        config_filename = config_name + ".csv"

        #Loading Models
        model = pickle.load(open('source_model/' + model_filename , 'rb'))

        #loading configrations
        config = pd.read_csv('source_config/' + config_filename)
        
        print(config)
        print(model)

        #Definition
        dict={}
    
        for i in range(len(config)):
            #param = config.iloc[i,0]
            #dict["var{0}".format(i+1)] = request.args.get(param)
            dict["var{0}".format(i+1)] = float(request.args.get(config.iloc[i,0]))
            
        values = dict.values()
        values_list = list(values)
        print(values_list)
        prediction = model.predict([values_list])
        return jsonify(prediction.tolist())
        # return 0




api.add_resource(Predict, '/predict')

# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug = False)
