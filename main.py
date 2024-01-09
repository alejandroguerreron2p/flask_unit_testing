from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config != None:
        app.config.update(test_config)

    # creates model
    class Book(Schema):
        title = fields.String(required=True)
        author = fields.String(required=True)

    from client import retrieve_book, create_book

    @app.route('/books/<book_id>', methods=['GET'])
    def get_book(book_id):
        return jsonify(retrieve_book(book_id))

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        schema = Book()
        try:
            result = schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400
        
        return jsonify(create_book(data))
    
    return app