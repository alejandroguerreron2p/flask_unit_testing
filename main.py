from flask import Flask, request, jsonify
from service import retrieve_book, create_book
from models.client import Client
 

def create_app(client, test_config=None):
    app = Flask(__name__)

    if test_config != None:
        app.config.update(test_config)
    
    repository = Client(client)

    @app.route('/books/<book_id>', methods=['GET'])
    def get_book(book_id):
        try:
            response = jsonify(repository.create_book(book_id))
            return response
        except:
            return response

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        try:
            response = jsonify(create_book(data))
            return response
        except:
            return response
        
    return app

