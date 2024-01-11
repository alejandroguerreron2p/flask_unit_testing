from interfaces.book_repository_interface import BookRepositoryInterface
from service.api_dict import test_data

class HashBookRepository(BookRepositoryInterface):
    def __init__(self, data: dict):
        super().__init__(self, test_data)
        
    def find_book_by_id(book_id):
        if int(book_id) in test_data:
            return test_data[int(book_id)]
        else:
            return {'error': 'Book not found'}
                
    def create_book(data):
        # Insert into Test Data dict
        test_data[len(test_data)+1] = data

        # Return the newly created book's ID
        return {'message': 'Book created successfully', 'book_id': str(len(test_data))}
    
    def update_book(book_id, data):
        test_data[book_id] = data
        return {'message': 'Book updated successfully', 'book_id': str(book_id)}
    
    def delete_book(book_id):
        test_data.pop(book_id)
        return {'message': 'Book deleted successfully', 'book_id': str(book_id)}
    
    
        