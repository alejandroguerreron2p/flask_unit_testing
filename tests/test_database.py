from database import retrieve_book_db, create_book_db
import pytest
from main import app, client  # Adjust the import based on your project structure

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_retrieve_book_db(mock_mongo):
    # Mock the MongoDB interaction
    mock_mongo.db.books.find_one.return_value = {'title': 'Test Book', 'author': 'Test Author'}

    # Call the database layer function
    result = retrieve_book_db('123', None)

    # Assert the expected result
    assert result == {'title': 'Test Book', 'author': 'Test Author'}

def test_create_book_db(mock_mongo):
    # Mock the MongoDB interaction
    mock_mongo.db.books.insert_one.return_value.inserted_id = '123'

    # Call the database layer function
    result = create_book_db({'title': 'Test Book', 'author': 'Test Author'}, None)

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': '123'}
