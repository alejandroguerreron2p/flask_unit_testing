from book_repository import HashBookRepository
from api_dict import test_data

def test_retrieve_book_db():
    # Call the database layer function
    result = HashBookRepository.find_book_by_id(2)

    # Assert the expected result
    assert result == {'title': '1984', 'author': 'George Orwell'}

def test_create_book_db():
    # Call the database layer function
    result = HashBookRepository.create_book({'title': 'Dune', 'author': 'Frank Herbert'})

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': str(len(test_data)) }