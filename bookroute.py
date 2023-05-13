from flask import Flask, jsonify, request
from book import Book

app = Flask(__name__)

# In-memory database of books
books = []

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book.id == id), None)
    if book is None:
        return 'Book not found', 404
    return jsonify(book)

# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.json
    id = len(books) + 1
    book = Book(id, book_data['name'], book_data['author'], book_data['publisher'])
    books.append(book)
    return jsonify(book)

# PUT (update) an existing book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book.id == id), None)
    if book is None:
        return 'Book not found', 404
    book_data = request.json
    book.name = book_data['name']
    book.author = book_data['author']
    book.publisher = book_data['publisher']
    return jsonify(book)

# DELETE a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book.id != id]
    return '', 204
