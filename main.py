from flask import Flask, request
from book_repository import HashBookRepository
from service import Service
from api_dict import test_data
 
def create_app(test_config=None):
    app = Flask(__name__)

    if test_config != None:
        app.config.update(test_config)
        
    book_repository = HashBookRepository(test_data)
    service = Service(book_repository)

    @app.route('/books/<book_id>', methods=['GET'])
    def get_book(book_id):
        response = service.retrieve_book(book_id)
        return response

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        try:
            response = service.create_book(data)
            return response
        except:
            return response
    
    return app