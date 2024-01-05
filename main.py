import os
from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

uri = os.environ["MONGO_URI"]
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

from client import retrieve_book, create_book

@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify(retrieve_book(book_id))

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    return jsonify(create_book(data))