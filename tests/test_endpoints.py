def test_get_book(client):
    # Assuming you have a book with ID '123' in your test database
    response = client.get('/books/1')

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json == {'title': 'Thus Spoke Zarathrusta', 'author': 'Friedrich Nietzsche'}

def test_retrieve_non_existent_book(client):
    response = client.get('/books/3')
    assert response.status_code == 400
    assert response.json == {"error": "Book not found"}

def test_add_book(client):
    # Data for creating a new book
    new_book_data = {'title': 'The Creative Act', 'author': 'Rick Rubin'}

    # Make a POST request to add a new book
    response = client.post('/books', json=new_book_data)
    
    new_id = response.json["book_id"]

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json == {'message': 'Book created successfully', 'book_id': new_id}  # Adjust book_id based on your actual response

    # Optionally, you can make a GET request to verify the new book has been added
    response = client.get(f'/books/{new_id}')  # Use the actual book_id from the previous response
    assert response.status_code == 200
    assert response.json == {'title': 'The Creative Act', 'author': 'Rick Rubin'}

def test_add_book_extra_values(client):
    # Tests that certain fields are unknown
    new_book_data = {'title': 'The Creative Act', 'author': 'Rick Rubin','unknown_value': 'super bad thing here!'}
    response = client.post('/books', json=new_book_data)
    assert response.status_code == 400
    assert response.json == {'error': {'unknown_value': ['Unknown field.']}}

def test_add_book_missing_author(client):
    # Tests that certain fields are unknown
    new_book_data = {'title': 'The Creative Act'}
    response = client.post('/books', json=new_book_data)
    assert response.status_code == 400
    assert response.json == {'error': {'author': ['Missing data for required field.']}}
    
def test_add_book_missing_title(client):
    # Tests that certain fields are unknown
    new_book_data = {'author': 'Rick Rubin'}
    response = client.post('/books', json=new_book_data)
    assert response.status_code == 400
    assert response.json == {'error': {'title': ['Missing data for required field.']}}

def test_update_book(client):
    # Data for creating a new book
    update_book_data = {'title': 'The Creative Act', 'author': 'Rick Rubin'}

    # Make a POST request to add a new book
    response = client.put('/books/1', json=update_book_data)

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json == {'message': 'Book updated successfully', 'book_id': '1'}  # Adjust book_id based on your actual response

    # Optionally, you can make a GET request to verify the new book has been added
    response = client.get(f'/books/1')  # Use the actual book_id from the previous response
    assert response.status_code == 200
    assert response.json == {'title': 'The Creative Act', 'author': 'Rick Rubin'}
    
def test_update_book_extra_values(client):
    # Tests that certain fields are unknown
    update_book_data = {'title': 'The Creative Act', 'author': 'Rick Rubin','unknown_value': 'super bad thing here!'}
    response = client.put('/books/1', json=update_book_data)
    assert response.status_code == 400
    assert response.json == {'error': {'unknown_value': ['Unknown field.']}}

def test_update_book_missing_title(client):
    # Tests that certain fields are unknown
    update_book_data = {'author': 'Rick Rubin'}
    response = client.put('/books/1', json=update_book_data)
    assert response.status_code == 400
    assert response.json == {'error': {'title': ['Missing data for required field.']}}
    
def test_update_book_missing_author(client):
    # Tests that certain fields are unknown
    new_book_data = {'title': 'The Creative Act'}
    response = client.put('/books/1', json=new_book_data)
    assert response.status_code == 400
    assert response.json == {'error': {'author': ['Missing data for required field.']}}
    
def test_update_unexisting_book(client):
    # Tests that certain fields are unknown
    new_book_data = {'title': 'The Creative Act', 'author': 'Rick Rubin'}
    response = client.put('/books/3', json=new_book_data)
    assert response.status_code == 400
    assert response.json == {'error': 'Book not found to update', 'book_id': '3'}
    
def test_delete_book(client):
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Book deleted successfully', 'book_id': '1'}
    
    response = client.get('/books/1')
    assert response.status_code == 400
    assert response.json == {'error': 'Book not found'}
    
def test_delete_unexisting_book(client):
    response = client.delete('/books/3')
    assert response.status_code == 400
    assert response.json == {'error': 'Book not found to delete', 'book_id': '3'}