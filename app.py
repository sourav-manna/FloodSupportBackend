import pymongo
from flask import Flask, render_template, request, url_for, redirect
from flask_cors import CORS
from pymongo import MongoClient
import json

# ...

app = Flask(__name__)
CORS(app)

#client = MongoClient('localhost', 27017, username='mannasourav525', password='CJ7f4VRVoBsKalXv')


client = pymongo.MongoClient("mongodb+srv://mannasourav525:CJ7f4VRVoBsKalXv@cluster0.mzbilrj.mongodb.net/?retryWrites=true&w=majority")


# Create a new database
db = client['database']

# Create a new collection
collection = db['usercollection']

# Define the schema for the collection
schema = {
    'name': {
        'type': 'string'
    },
    'email': {
        'type': 'integer'
    },
    'password': {
        'type': 'string'
    },
    'category': {
        'type': 'string'
    }
}

@app.route('/signup', methods=['POST'])
def insert():
    # Insert data into the collection
    getdata = request.get_json()
    if collection.find_one({'email': getdata['email']}) is None:
        data = {
            'name': getdata['name'],
            'password': getdata['password'],
            'email': getdata['email'],
            'category': getdata['category']
        }
        collection.insert_one(data)
        return {"message": "Data inserted successfully", "status": True}
    else:
        return {"message":"Email already exists", "status": False}

#login route
@app.route('/login', methods=['POST'])
def login():
    getdata = request.get_json()
    data = {
        'email': getdata['email'],
        'password': getdata['password']
    }
    #print(data)
    log_data = collection.find_one(data)
    if collection.find_one(data) is None:
        return {"message":"Invalid credentials","status": True}
    else:
        return {"docs":{"name": log_data['name'], "category": log_data['category']}, "status": True}

app.run()

