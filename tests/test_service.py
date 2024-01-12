from book_repository import HashBookRepository
from service import Service
from api_dict import test_data

service = Service(HashBookRepository(test_data))

def test_retrieve_book():
    # Call the client layer function
    result = service.retrieve_book(1)

    # Assert the expected result
    assert result == {'title': 'Thus Spoke Zarathrusta', 'author': 'Friedrich Nietzsche'}

def test_retrieve_non_existent_book():
    result = service.retrieve_book(3)
    assert result == {"error": "Book not found"}

def test_create_book():
    # Call the client layer function
    result = service.create_book({'title': 'The Creative Act', 'author': 'Rick Rubin'})

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': str(len(test_data))}
