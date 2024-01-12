from flask import jsonify
from marshmallow import ValidationError
from book_repository import HashBookRepository
from book import Book

class Service():
    def __init__(self, data):
        super().__init__(data)
        
    def retrieve_book(book_id):
        return HashBookRepository.find_book_by_id(book_id)

    def create_book(data):
        schema = Book()
        try:
            result = schema.load(data)
            if result:
                return HashBookRepository.create_book(data)
        except ValidationError as err:
            return jsonify(err.messages), 400
    