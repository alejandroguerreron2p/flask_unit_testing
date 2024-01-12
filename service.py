from flask import jsonify
from marshmallow import ValidationError
from book_repository import BookRepositoryInterface
from book import Book

class Service():
    def __init__(self, book_repo):
        self.book_repo = book_repo
        
    def retrieve_book(self, book_id):
        return self.book_repo.find_book_by_id(book_id)

    def create_book(self, data):
        schema = Book()
        try:
            result = schema.load(data)
            if result:
                return self.book_repo.create_book(data)
        except ValidationError as err:
            return jsonify(err.messages), 400
    