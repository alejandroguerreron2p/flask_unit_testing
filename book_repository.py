import uuid

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
        if book_id in self.data:
            return self.data[book_id]
        else:
            return {'error': 'Book not found'}
                
    def create_book(self, data):
        # Insert into Test Data dict
        new_id = str(uuid.uuid4())
        self.data[new_id] = data
        # Return the newly created book's ID
        return {'message': 'Book created successfully', 'book_id': new_id}
    
    def update_book(self, book_id, data):
        if book_id in self.data:
            self.data.update({book_id: data})
            return {'message': 'Book updated successfully', 'book_id': book_id}
        else:
            return {'error': 'Book not found to update', 'book_id': book_id}
    
    def delete_book(self, book_id):
        if book_id in self.data:
            self.data.pop(book_id)
            return {'message': 'Book deleted successfully', 'book_id': book_id}
        else:
            return {'error': 'Book not found to delete', 'book_id': book_id}