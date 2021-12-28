from flask import Flask, jsonify, request
from flask_restful import Resource, Api
# import pickle
import numpy as np
# import json
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import cv2
# import glob
# import os.path

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

        #=========REQUIREMENT=========#
        input_format = request.form.get("input_format")


        if input_format == 'value' :
            
            #Loading Models
            #=========REQUIREMENT=========#
            model_name = request.form.get("model")
            model_filename = model_name + ".pkl"
            model = joblib.load('source_model/' + model_filename )

            #loading configrations
            #=========REQUIREMENT=========#
            config_name = request.form.get("config")       
            config_filename = config_name + ".csv"
            config = pd.read_csv('source_config/' + config_filename)
            
            print(config)
            print(model)

            #Definition
            dict={}    
            for i in range(len(config)):
                dict["var{0}".format(i+1)] = float(request.form.get(config.iloc[i,0]))
                
            values = dict.values()
            values_list = list(values)
            print(values_list)
            prediction = model.predict([values_list])
            output = jsonify(prediction.tolist())

        elif input_format == 'file' :

            #Loading Models
            #=========REQUIREMENT=========#
            model_name = request.form.get("model")
            model_filename = model_name + ".pkl"
            model = joblib.load('source_model/' + model_filename )

            #=========REQUIREMENT=========#
            data = request.files["file"]
            data = pd.read_csv(data)

            prediction = model.predict(data)
            output = jsonify(prediction.tolist())

        
        elif input_format == 'text' :        
            #Loading Models
            #=========REQUIREMENT=========#
            model_name = request.form.get("model")
            model_filename = model_name + ".pkl"
            model = joblib.load('source_model/' + model_filename )

            #Load count vector from disk
            cv = joblib.load(open('source_model/model_sentiment_transform.pkl','rb'))
            #Load the vocabulary
            words = joblib.load(open('source_model/model_sentiment_vocabulary.pkl','rb'))

            #loading text data from user
            #=========REQUIREMENT=========#
            text = request.form.get("text")
            data = [text]

            countVect = CountVectorizer(vocabulary=words)
            sentence = countVect.transform(data).toarray()

            # vectorize the user's query and make a prediction
            review_prediction = model.predict(sentence)[0]
            review_prediction_probablity = model.predict_proba(sentence)
                    
            # Output either 'Negative' or 'Positive' along with the score
            if review_prediction == 0:
                pred_text = 'Negative'
                confidence = review_prediction_probablity[0][0]
            else:
                pred_text = 'Positive'
                confidence = review_prediction_probablity[0][1]

            # create JSON object
            output = {'prediction': pred_text, 'confidence': confidence}   

                    
        elif input_format == 'image' : 
            #=========REQUIREMENT=========# 
            prototxt = request.form.get("prototxt")
            #=========REQUIREMENT=========#
            caffemodel = request.form.get("caffemodel")
            #=========REQUIREMENT=========#
            npy = request.form.get("npy")       
            net = cv2.dnn.readNetFromCaffe('./source_model/' + prototxt,'./source_model/' + caffemodel)
            pts = np.load('./source_model/' + npy)
            class8 = net.getLayerId("class8_ab")
            conv8 = net.getLayerId("conv8_313_rh")
            pts = pts.transpose().reshape(2,313,1,1)
            net.getLayer(class8).blobs = [pts.astype("float32")]
            net.getLayer(conv8).blobs = [np.full([1,313],2.606,dtype='float32')]

            #=========REQUIREMENT=========#
            filestr = request.files['image'].read()
            #convert string data to numpy array
            npimg = np.fromstring(filestr, np.uint8)
            # convert numpy array to image
            image = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
            
            scaled = image.astype("float32")/255.0
            lab = cv2.cvtColor(scaled,cv2.COLOR_BGR2LAB)


            resized = cv2.resize(lab,(224,224))
            L = cv2.split(resized)[0]
            L -= 50


            net.setInput(cv2.dnn.blobFromImage(L))
            ab = net.forward()[0, :, :, :].transpose((1,2,0))

            ab = cv2.resize(ab, (image.shape[1],image.shape[0]))

            L = cv2.split(lab)[0]
            colorized = np.concatenate((L[:,:,np.newaxis], ab), axis=2)

            colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)
            colorized = np.clip(colorized,0,1)

            colorized = (255 * colorized).astype("uint8")

            cv2.imshow("Original",image)
            cv2.imshow("Colorized",colorized)

            cv2.waitKey(0)
            output = 0

        return output


api.add_resource(Predict, '/predict')

# driver function
if __name__ == '__main__':
    #app.run(host="0.0.0.0",port=5005,debug=True)
    app.run(host="0.0.0.0",port=5000,debug=False)
