from business_logic import retrieve_book_logic, create_book_logic
from api_dict import test_data

def test_retrieve_book_logic():

    # Call the business logic layer function
    result = retrieve_book_logic(1)

    # Assert the expected result
    assert result == {'title': 'Thus Spoke Zarathrusta', 'author': 'Friedrich Nietzsche'}

def test_create_book_logic():
    # Call the business logic layer function
    result = create_book_logic({'title': 'The Creative Act', 'author': 'Rick Rubin'})

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': str(len(test_data))}