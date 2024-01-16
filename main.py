from flask import Flask, jsonify, request
from book_repository import HashBookRepository
from service import Service
from api_dict import test_data
 
def create_app(test_config=None):
    app = Flask(__name__)

    if test_config != None:
        app.config.update(test_config)
        copy_td = test_data.copy()
        book_repository = HashBookRepository(copy_td)
        service = Service(book_repository)
    else:
        book_repository = HashBookRepository(test_data)
        service = Service(book_repository)

    @app.route('/books/<book_id>', methods=['GET'])
    def get_book(book_id):
        response = service.retrieve_book(book_id)
        if "error" not in response:
            return jsonify(response), 200
        else:
            return jsonify(response), 400

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        response = service.create_book(data)
        if "error" not in response:
            return jsonify(response), 200
        else:
            return jsonify(response), 400 
        
    @app.route('/books/<book_id>', methods=['PUT'])
    def update_book(book_id):
        data = request.get_json()
        response = service.update_book(book_id, data)
        if "error" not in response:
            return jsonify(response), 200
        else:
            return jsonify(response), 400 
        
    @app.route('/books/<book_id>', methods=['DELETE'])
    def delete_book(book_id):
        response = service.delete_book(book_id)
        if "error" not in response:
            return jsonify(response), 200
        else:
            return jsonify(response), 400 
    
    return app