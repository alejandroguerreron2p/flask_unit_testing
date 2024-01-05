from database import retrieve_book_db, create_book_db

def retrieve_book_logic(book_id):
    # Business logic can be added here if needed
    return retrieve_book_db(book_id)

def create_book_logic(data):
    # Business logic can be added here if needed
    return create_book_db(data)