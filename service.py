from marshmallow import ValidationError
from book import Book

class ServiceInterface():
    def retrieve_book(self, book_id):
        raise NotImplementedError
    def create_book(self, data):
        raise NotImplementedError
    def update_book(self, book_id, data):
        raise NotImplementedError
    def delete_book(self, book):
        raise NotImplementedError

class Service():
    def __init__(self, book_repo):
        self.book_repo = book_repo
        
    def retrieve_book(self, book_id):
        result = self.book_repo.find_book_by_id(book_id)
        return result

    def create_book(self, data):
        schema = Book()
        try:
            schema.load(data)
            result = self.book_repo.create_book(data) 
            return result
        except ValidationError as err:
            return {"error": err.messages}
        
    def update_book(self, book_id, data):
        schema = Book() 
        try:
            schema.load(data)
            result = self.book_repo.update_book(book_id, data)
            return result
        except ValidationError as err:
            return {"error": err.messages}
        
    def delete_book(self, book_id):
        result = self.book_repo.delete_book(book_id)
        return result
    