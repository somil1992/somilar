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


# class Predict(Resource):
#     def post(self):

        model = request.args.get("model")
        config = request.args.get("config")
        
        model_filename = model
        config_filename = pickle.load(open(filename, 'rb'))

        # #Loading Models
        # model = pickle.load(open('model/model.pkl', 'rb'))

        # #loading configrations
        # config=pd.read_csv('config/config.csv')

#         #Definition
#         dict={}
    
#         for i in range(len(config)):
#             #param = config.iloc[i,0]
#             #dict["var{0}".format(i+1)] = request.args.get(param)
#             dict["var{0}".format(i+1)] = request.args.get(config.iloc[i,0])
            
#         values = dict.values()
#         values_list = list(values)

#         prediction = model.predict([values_list])
#         return jsonify(prediction.tolist())



# api.add_resource(Predict, '/predict')

# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug = False)

