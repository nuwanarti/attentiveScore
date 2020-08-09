from flask_restplus import Resource
from flask import Flask, jsonify, request
import json
from PIL import Image
import cv2
# import pandas as pd
from . import api

# from regressor import fun
from . import regressor
# from regressor import fun


class Status(Resource):
    def post(self):
        return {
            "status": "Up and running"
        }, 200

class RegressionOut(Resource):
    def post(self):
        # print(self.get_json())
        
        json_data = request.get_json(force=True)
        # print(json_data['faceParams'])
        # json_mylist = json.dumps(json_data['faceParams'], separators=(',', ':'))
        # print(json_mylist)
        faces = json_data['faceParams']
        # df = pd.load_json(faces)
        # print(df.head())
        # for face in faces:
        #     print(face['name'])
        value = regressor.fun(faces)
        return{
            "mean": value,
            "probability": 0.75
        }, 200

class BodyLang(Resource):
    def post(self):
        print('hi there')
        json_data = request.get_json(force=True)
        images = json_data['images']
        imgArray = []
        for img in images:
            imgdata = base64.b64decode(str(img))
            m = Image.open(io.BytesIO(imgdata))
            imgArray.append(cv2.cvtColor(np.array(m), cv2.COLOR_BGR2RGB))
        print(imgArray)
        # value = 
        return {
            "status": "done"
        }, 200, {'Access-Control-Allow-Origin': '*'}

class DB(Resource):
    def get(self):
        # print('came here')
        return {
            "db": "Database here"
        }, 200

# from flask_cors import CORS, cross_origin
# cors = CORS(api)
# api.config['CORS_HEADERS'] = 'Content-Type'

api.add_resource(Status, '/status')
api.add_resource(RegressionOut, '/regression')
api.add_resource(DB, '/db')
api.add_resource(BodyLang, '/bodyLang')