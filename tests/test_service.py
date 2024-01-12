from service import Service
from api_dict import test_data

def test_retrieve_book():
    # Call the client layer function
    result = Service.retrieve_book(1)

    # Assert the expected result
    assert result == {'title': 'Thus Spoke Zarathrusta', 'author': 'Friedrich Nietzsche'}


def test_create_book():
    # Call the client layer function
    result = Service.create_book({'title': 'The Creative Act', 'author': 'Rick Rubin'})

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': str(len(test_data))}
