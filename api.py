from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Initialize Flask
app = Flask(__name__)
api = Api(app)

# A List of Dicts to store all of the books
books = [{
    "id": 1,
    "title": "Zero to One",
    "author": "Peter Thiel",
    "length": 195,
    "rating": 4.17
},
    {
    "id": 2,
    "title": "Atomic Habits ",
    "author": "James Clear",
    "length": 319,
    "rating": 4.35
}
]

# Schema For the Book Request JSON
bookFields = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String,
    "length": fields.Integer,
    "rating": fields.Float
}


# -------------------------------- Book Class -------------------------------- #


# Resource: Individual Book Routes
@api.resource('/books/<int:id>')
class Book(Resource):
    def __init__(self):
        # Initialize The Flask Request Parser and add arguments as in an expected request
        # Allows you easy access to any variable on the flask.request and also validates the response based on the arguments provided
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str, location="json")
        self.reqparse.add_argument("author", type=str, location="json")
        self.reqparse.add_argument("length", type=int, location="json")
        self.reqparse.add_argument("rating", type=float, location="json")

        super(Book, self).__init__()

    # GET - Returns a single book object given a matching id
    def get(self, id):
        book = [book for book in books if book['id'] == id]

        if(len(book) == 0):
            abort(404)

        return{"book": marshal(book[0], bookFields)}
        # The marshal method just makes sure the object that is being returned is being filtered through the fields defined in the bookFields dict schema.

    # PUT - Given an id
    def put(self, id):
        book = [book for book in books if book['id'] == id]

        if len(book) == 0:
            abort(404)

        book = book[0]

        # Loop Through all the passed agruments
        args = self.reqparse.parse_args()
        for k, v in args.items():
            # Check if the passed value is not null
            if v is not None:
                # if not, set the element in the books dict with the 'k' object to the value provided in the request.
                book[k] = v

        return{"book": marshal(book, bookFields)}

        # Delete - Given an id
    def delete(self, id):
        book = [book for book in books if book['id'] == id]

        if(len(book) == 0):
            abort(404)

        books.remove(book[0])

        return 201


# ------------------------------ Booklist Class ------------------------------ #


# This class contains the routes dealing with operations on the entire database.
@api.resource('/books')
class BookList(Resource):
    def __init__(self):
        # Init method initializes the request parser. It parses the request JSON Object and also validates it based on the arguments provided.
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "title", type=str, required=True, help="The title of the book must be provided", location="json")
        self.reqparse.add_argument(
            "author", type=str, required=True, help="The author of the book must be provided", location="json")
        self.reqparse.add_argument("length", type=int, required=True,
                                   help="The length of the book (in pages)", location="json")
        self.reqparse.add_argument(
            "rating", type=float, required=True, help="The rating must be provided", location="json")

    # simply returns all the elements in the books list
    def get(self):
        return{"books": [marshal(book, bookFields) for book in books]}

    # takes a JSON Object. Parses it , creates a new dict and appends it to the Books list.
    def post(self):
        args = self.reqparse.parse_args()
        book = {
            "id": books[-1]['id'] + 1 if len(books) > 0 else 1,
            "title": args["title"],
            "author": args["author"],
            "length": args["length"],
            "rating": args["rating"]
        }

        books.append(book)
        return{"book": marshal(book, bookFields)}, 201



if __name__ == "__main__":
    app.run(debug=True)