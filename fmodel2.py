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
model = pickle.load(open('model.pkl', 'rb'))
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
class Predict(Resource):
    def post(self):
        print("here")
        data = request.files["kk"]
        # data = request.form['gdp']
        data = pd.read_csv(data)
        data.set_index("date", inplace = True)
        print(data)
        print("out")
        print("auto build")
        print("auto build1")
#       print("auto build")
             
        prediction = model.predict(n_periods = 60, exogenous = data)

        output_list = []
        for i in prediction:
            output_list.append(i)
        output = pd.DataFrame()
        output["Date"] = data.index
        output["prediction"] = output_list
        output.to_csv("prediction1.csv",index = False)        
        return output.to_json()



api.add_resource(Predict, '/forecast2')

# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug = False)

