from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
import json
from flask_jsonpify import jsonify
from bin.functions import *
import pymysql

import random

app = Flask('Suffix-Converter')
api = Api(app)

class mainclass(Resource):
    def get(self):
        json = {"status": {"code": '200',"message": "ok"}}
        return json

class Converter(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sc', required=True, type=int, help="")
        parser.add_argument('txt', required=True, type=str, help="")
        parser.add_argument('before', required=True, type=str, help="")
        parser.add_argument('after', required=True, type=str, help="")
        args = parser.parse_args() 

        sc = args['sc']
        txt = args['txt']
        before = args['before']
        after = args['after']

        result = convert_text(sc, txt, before, after)

        return result


api.add_resource(mainclass, '/')
api.add_resource(Converter, '/api/v1')

if __name__ == '__main__':
    app.run(port=1234, host="127.0.0.1", debug=True)