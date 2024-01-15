import os
import pytest
from book_repository import HashBookRepository
from api_dict import test_data

@pytest.fixture
def setup_data():
    yield test_data

def test_retrieve_book_db(setup_data):
    result = setup_data.find_book_by_id(2)
    assert result == {'title': '1984', 'author': 'George Orwell'}

def test_retrieve_non_existent_book_db(setup_data):
    result = setup_data.find_book_by_id(3)
    assert result == {"error": "Book not found"}

def test_create_book_db(setup_data):
    result = setup_data.create_book({'title': 'Dune', 'author': 'Frank Herbert'})
    assert result == {'message': 'Book created successfully', 'book_id': str(len(test_data)) }

def test_clean_files(setup_data):
    assert len(setup_data.data) == 2