from flask_pymongo import PyMongo
from pymongo import MongoClient

# Setup MongoDB here
# mongo = PyMongo(uri="mongodb://localhost:27017/database")
mongo = MongoClient('mongodb://localhost:27017/')
db = mongo['github_webhooks']
events_collection = db['events']