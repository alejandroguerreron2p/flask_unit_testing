from bson.objectid import ObjectId
from main import client

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author
        }

def retrieve_book_db(book_id, Book):
    # Convert string to ObjectId for MongoDB query
    book_object_id = ObjectId(book_id)
    book_data = client.db.books.find_one({'_id': book_object_id})

    if book_data:
        # Create Book object from MongoDB data
        book = Book(book_data['title'], book_data['author'])
        return book.to_dict()
    else:
        return {'error': 'Book not found'}

def create_book_db(data, Book):
    # Create Book object from request data
    new_book = Book(data['title'], data['author'])

    # Insert into MongoDB
    result = client.db.books.insert_one(new_book.to_dict())

    # Return the newly created book's ID
    return {'message': 'Book created successfully', 'book_id': str(result.inserted_id)}