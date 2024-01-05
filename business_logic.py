from database import retrieve_book_db, create_book_db
from database import Book

def retrieve_book_logic(book_id):
    # Business logic can be added here if needed
    return retrieve_book_db(book_id, Book)

def create_book_logic(data):
    # Business logic can be added here if needed
    return create_book_db(data, Book)