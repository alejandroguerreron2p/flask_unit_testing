import pytest
from book_repository import HashBookRepository
from service import Service, ServiceInterface
from api_dict import test_data

@pytest.fixture
def service():
    copy_td = test_data.copy()
    service  = Service(HashBookRepository(copy_td))
    yield service

def test_retrieve_book(service):
    # Call the client layer function
    result = service.retrieve_book('1')

    # Assert the expected result
    assert result == {'title': 'Thus Spoke Zarathrusta', 'author': 'Friedrich Nietzsche'}

def test_retrieve_non_existent_book(service):
    result = service.retrieve_book('3')
    assert result == {"error": "Book not found"}

def test_create_book(service):
    # Call the client layer function
    result = service.create_book({'title': 'The Creative Act', 'author': 'Rick Rubin'})
    
    new_id = result["book_id"]

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': new_id}

def test_update_book_db(service):
    result = service.update_book('2', {'title': 'Dune', 'author': 'Frank Herbert'})
    assert result == {'message': 'Book updated successfully', 'book_id': '2'}
    
    result = service.retrieve_book('2')
    assert result == {'title': 'Dune', 'author': 'Frank Herbert'}
    
def test_update_unexisting_book_db(service):
    result = service.update_book('3', {'title': 'Dune', 'author': 'Frank Herbert'})
    assert result == {'error': 'Book not found to update', 'book_id': '3'}
    
def test_delete_book_db(service):
    result = service.delete_book('1')
    assert result == {'message': 'Book deleted successfully', 'book_id': '1'}
    
    result = service.retrieve_book('1')
    assert result == {"error": "Book not found"}   
    
def test_delete_unexisting_book_db(service):
    result = service.delete_book('3')
    assert result == {'error': 'Book not found to delete', 'book_id': '3'}