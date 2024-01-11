from flask import jsonify
from database import create_book_db, retrieve_book_db
from models.book import Book
from marshmallow import ValidationError

def retrieve_book(book_id):
    return retrieve_book_db(book_id)

def create_book(data):
    schema = Book()
    try:
        result = schema.load(data)
        if result:
            return create_book_db(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    