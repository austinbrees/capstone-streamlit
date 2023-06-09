from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from pymysql import connect
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from flask_restx import Api, Namespace, Resource, reqparse
import json


load_dotenv()

MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')


app = Flask(__name__)
api = Api(app)


limit_parser = reqparse.RequestParser()
limit_parser.add_argument('limit', type=int, default=10000)

try:
    client =  pymongo.MongoClient(
        "mongodb+srv://{0}:{1}@{2}/?retryWrites=true&w=majority" \
        .format(MONGO_USER, MONGO_PASS, MONGO_HOST))
    db = client[MONGO_DATABASE]
except pymongo.errors.ConnectionFailure as e:
    print("Failed to connect to MongoDB instance: %s" % e)
    
def convert_id_to_str(data_dicts):
    for data_dict in data_dicts:
        if '_id' in data_dict:
            data_dict['_id'] = str(data_dict['_id']['$oid'])
    return data_dicts

class Articles(Resource):
    def get(self):
        args = limit_parser.parse_args()
        limit = args['limit']
        collection = db['articles']
        data = collection.find().limit(limit)
        data_dicts = json.loads(dumps(data))
        data_dicts = convert_id_to_str(data_dicts)
        return data_dicts, 200

class Transactions(Resource):
    def get(self):
        args = limit_parser.parse_args()
        limit = args['limit']
        collection = db['transactions']
        data = collection.find().limit(limit)
        data_dicts = json.loads(dumps(data))
        data_dicts = convert_id_to_str(data_dicts)
        return data_dicts, 200

class Customers(Resource):
    def get(self):
        args = limit_parser.parse_args()
        limit = args['limit']
        collection = db['customers']
        data = collection.find().limit(limit)
        data_dicts = json.loads(dumps(data))
        data_dicts = convert_id_to_str(data_dicts)
        return data_dicts, 200

api.add_resource(Articles, "/api/articles")
api.add_resource(Transactions, "/api/transactions")
api.add_resource(Customers, "/api/customers")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 8000, debug=True)