from flask import Flask, request, jsonify

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config != None:
        app.config.update(test_config)

    from client import retrieve_book, create_book

    @app.route('/books/<book_id>', methods=['GET'])
    def get_book(book_id):
        return jsonify(retrieve_book(book_id))

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        return jsonify(create_book(data))
    
    return app