from client import retrieve_book, create_book
from unittest.mock import patch

@patch('client.retrieve_book_logic')
def test_retrieve_book(mock_retrieve_book_logic):
    # Mock the business logic layer
    mock_retrieve_book_logic.return_value = {'title': 'Test Book', 'author': 'Test Author'}

    # Call the client layer function
    result = retrieve_book('123')

    # Assert the expected result
    assert result == {'title': 'Test Book', 'author': 'Test Author'}

@patch('client.create_book_logic')
def test_create_book(mock_create_book_logic):
    # Mock the business logic layer
    mock_create_book_logic.return_value = {'message': 'Book created successfully', 'book_id': '123'}

    # Call the client layer function
    result = create_book({'title': 'Test Book', 'author': 'Test Author'})

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': '123'}
