from api_dict import test_data

def retrieve_book_db(book_id):
    if int(book_id) in test_data:
        return test_data[int(book_id)]
    else:
        return {'error': 'Book not found'}

def create_book_db(data):
    # Insert into Test Data dict
    test_data[len(test_data)+1] = data

    # Return the newly created book's ID
    return {'message': 'Book created successfully', 'book_id': str(len(test_data))}