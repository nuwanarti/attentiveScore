from flask_restplus import Resource
from flask import Flask, jsonify, request
import json
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


class DB(Resource):
    def get(self):
        return {
            "db": "Database here"
        }, 200


api.add_resource(Status, '/status')
api.add_resource(RegressionOut, '/regression')
api.add_resource(DB, '/db')

