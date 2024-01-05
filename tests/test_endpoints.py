import json
from main import app  # Assuming your Flask app is in a file named app.py

def test_get_book():
    client = app.test_client()

    # Assuming you have a book with ID '123' in your test database
    response = client.get('/books/123')

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json == {'title': 'Test Book', 'author': 'Test Author'}

def test_add_book():
    client = app.test_client()

    # Data for creating a new book
    new_book_data = {'title': 'New Book', 'author': 'New Author'}

    # Make a POST request to add a new book
    response = client.post('/books', json=new_book_data)

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json == {'message': 'Book created successfully', 'book_id': '123'}  # Adjust book_id based on your actual response

    # Optionally, you can make a GET request to verify the new book has been added
    response = client.get('/books/123')  # Use the actual book_id from the previous response
    assert response.status_code == 200
    assert response.json == {'title': 'New Book', 'author': 'New Author'}
