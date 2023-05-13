from flask import Flask
from bookRoute import *

app = Flask(__name__)
app.register_blueprint(book_routes)

if __name__ == '__main__':
    app.run(debug=True)
