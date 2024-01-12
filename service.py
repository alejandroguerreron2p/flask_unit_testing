from flask import jsonify
from marshmallow import ValidationError
from book import Book
from book_repository import BookRepositoryInterface

class ServiceInterface():
    def retrieve_book(self, book_id):
        pass
    def create_book(self, data):
        pass
    def update_book(self, book_id, data):
        pass
    def delete_book(self, book):
        pass

class Service():
    def __init__(self, book_repo):
        self.book_repo = book_repo
        
    def retrieve_book(self, book_id):
        result = self.book_repo.find_book_by_id(book_id)
        if "error" not in result:
            return result
        else:
            return jsonify(result), 400

    def create_book(self, data):
        schema = Book()
        try:
            validation = schema.load(data)
            if validation:
                result = self.book_repo.create_book(data) 
                return result
        except ValidationError as err:
            return jsonify(err.messages), 400
    