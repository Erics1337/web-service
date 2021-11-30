from flask import Flask
from flask_restful import Resource, Api, reqparse, inputs, abort

# Initialize Flask
app = Flask(__name__)
api = Api(app)

transactions = [
    # {"payer": "DANNON", "points": 200, "timestamp": "2020-11-02T14:00:00Z"},
    # {"payer": "CHIOBANI", "points": 500, "timestamp": "2020-13-02T14:00:00Z"},
    # {"payer": "SUBARU", "points": 400, "timestamp": "2020-12-02T14:00:00Z"}
    ]

@api.resource('/transactions')
class Transactions(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("payer", type=str, location="json")
        self.reqparse.add_argument("points", type=int, location="json")
        self.reqparse.add_argument("timestamp", type=str, location="json")

        super(Transactions, self).__init__()
    
    # Returns list of payer point balance objects
    def get(self):
        return{"transactions": transactions}, 200


    # Adds transactions for a specific payer and date
    def post(self):
        args = self.reqparse.parse_args()
        
        transaction = {
        "payer": args["payer"],
        "points": args["points"],
        "timestamp": args["timestamp"],
        }
        transactions.append(transaction)
            
        return {"Message": "Entry Submitted Successfuly"}, 201


    # Spend points using the rules above and return a list of { "payer": <string>, "points": <integer> } for each call.
    def put(self):
        args = self.reqparse.parse_args()
        points = args['points']
        
        transactions.sort(key = lambda x:x['timestamp'])

        # case 1: oldest transaction has enough points to spend request points
        # case 2: not enough points to spend in one transaction, spend what you can and 
        # check if next oldest transaction can spend the remainder; repeat until there are no more transactions to spend points on

        i = 0
        while i+1 <= len(transactions) and points != 0:
            if transactions[i]['points'] >= points:
                transactions[i]['points'] -= points
                break
            else:
                points -= transactions[i]['points']
                transactions[i]['points'] = 0
                if i+1 == len(transactions):
                    abort(400, description="Not enough points")
                i += 1

        transNoTime = [{k: v for k, v in d.items() if k != 'timestamp'} for d in transactions]

        return {"transactions": transNoTime}, 200



if __name__ == "__main__":
    app.run(debug=True)