from service.api_dict import test_data

def test_get_book(client):
    # Assuming you have a book with ID '123' in your test database
    response = client.get('/books/1')

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json == {'title': 'Thus Spoke Zarathrusta', 'author': 'Friedrich Nietzsche'}

def test_add_book(client):
    # Data for creating a new book
    new_book_data = {'title': 'The Creative Act', 'author': 'Rick Rubin'}

    # Make a POST request to add a new book
    response = client.post('/books', json=new_book_data)

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.json == {'message': 'Book created successfully', 'book_id': str(len(test_data))}  # Adjust book_id based on your actual response

    # Optionally, you can make a GET request to verify the new book has been added
    response = client.get(f'/books/{str(len(test_data))}')  # Use the actual book_id from the previous response
    assert response.status_code == 200
    assert response.json == {'title': 'The Creative Act', 'author': 'Rick Rubin'}

def test_add_book_extra_values(client):
    # Tests that certain fields are unknown
    new_book_data = {'title': 'The Creative Act', 'author': 'Rick Rubin','unknown_value': 'super bad thing here!'}
    response = client.post('/books', json=new_book_data)
    assert response.status_code == 400
    assert response.json == {"unknown_value": ["Unknown field."]}

def test_add_book_missing_values(client):
    # Tests that certain fields are unknown
    new_book_data = {'title': 'The Creative Act'}
    response = client.post('/books', json=new_book_data)
    assert response.status_code == 400
    assert response.json == {"author": ["Missing data for required field."]}
