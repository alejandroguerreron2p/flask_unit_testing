from api_dict import test_data

class BookRepositoryInterface:
    def find_book_by_id(self, book_id):
        pass
    def create_book(self, data):
        pass
    def update_book(self, book_id, data):
        pass
    def delete_book(self, book_id):
        pass

class HashBookRepository(BookRepositoryInterface):
    def __init__(self, data: dict):
        self.data = data
        
    def find_book_by_id(self, book_id):
        if int(book_id) in self.data:
            return self.data[int(book_id)]
        else:
            return {'error': 'Book not found'}
                
    def create_book(self, data):
        # Insert into Test Data dict
        self.data[len(self.data)+1] = data

        # Return the newly created book's ID
        return {'message': 'Book created successfully', 'book_id': str(len(self.data))}
    
    def update_book(self, book_id, data):
        self.data[book_id] = data
        return {'message': 'Book updated successfully', 'book_id': str(book_id)}
    
    def delete_book(self, book_id):
        self.data.pop(book_id)
        return {'message': 'Book deleted successfully', 'book_id': str(book_id)}
        
        