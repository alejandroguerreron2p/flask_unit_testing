from business_logic import retrieve_book_logic, create_book_logic

def retrieve_book(book_id):
    return retrieve_book_logic(book_id)

def create_book(data):
    return create_book_logic(data)