from flask import Flask, request, jsonify
from service.service import Service
 
def create_app(test_config=None):
    app = Flask(__name__)

    if test_config != None:
        app.config.update(test_config)

    @app.route('/books/<book_id>', methods=['GET'])
    def get_book(book_id):
        try:
            response = jsonify(Service.retrieve_book(book_id))
            return response
        except:
            return response

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        try:
            response = jsonify(Service.create_book(data))
            return response
        except:
            return response
        
    return app

