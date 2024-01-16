import os
import pytest
from book_repository import HashBookRepository
from api_dict import test_data

@pytest.fixture
def setup_data():
    copy_td = test_data.copy()
    book_repo = HashBookRepository(copy_td)
    yield book_repo

def test_retrieve_book_db(setup_data):
    result = setup_data.find_book_by_id('2')
    assert result == {'title': '1984', 'author': 'George Orwell'}

def test_retrieve_non_existent_book_db(setup_data):
    result = setup_data.find_book_by_id('3')
    assert result == {"error": "Book not found"}

def test_create_book_db(setup_data):
    result = setup_data.create_book({'title': 'Dune', 'author': 'Frank Herbert'})
    new_id = result["book_id"]
    assert result == {'message': 'Book created successfully', 'book_id': new_id }
    
def test_update_book_db(setup_data):
    result = setup_data.update_book('2', {'title': 'Dune', 'author': 'Frank Herbert'})
    assert result == {'message': 'Book updated successfully', 'book_id': str(len(setup_data.data)) }
    
    result = setup_data.find_book_by_id('2')
    assert result == {'title': 'Dune', 'author': 'Frank Herbert'}
    
def test_update_unexisting_book_db(setup_data):
    result = setup_data.update_book('3', {'title': 'Dune', 'author': 'Frank Herbert'})
    assert result == {'error': 'Book not found to update', 'book_id': '3'}
    
def test_delete_book_db(setup_data):
    result = setup_data.delete_book('1')
    assert result == {'message': 'Book deleted successfully', 'book_id': '1'}
    
    result = setup_data.find_book_by_id('1')
    assert result == {"error": "Book not found"}     
    
def test_delete_unexisting_book_db(setup_data):
    result = setup_data.delete_book('3')
    assert result == {'error': 'Book not found to delete', 'book_id': '3'}