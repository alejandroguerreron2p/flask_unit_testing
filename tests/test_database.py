from database import retrieve_book_db, create_book_db
from api_dict import test_data

def test_retrieve_book_db():
    # Call the database layer function
    result = retrieve_book_db(2)

    # Assert the expected result
    assert result == {'title': '1984', 'author': 'George Orwell'}

def test_create_book_db():
    # Call the database layer function
    result = create_book_db({'title': 'Dune', 'author': 'Frank Herbert'})

    # Assert the expected result
    assert result == {'message': 'Book created successfully', 'book_id': str(len(test_data)) }
