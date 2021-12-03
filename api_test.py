import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/transactions"
    TRANSACTION = {
                "payer": "SUBARU", 
                "points": 400, 
                "timestamp": "2020-12-02T14:00:00Z"
                }
    NEW_TRANSACTION = [{
                "payer": "SUBARU", 
                "points": 300
                }]
    POINTS = { "points": 100 }

    # GET request to /transactions returns the details of all transactions on account
    def test_1_get_all_transactions(self):
        r = requests.get(ApiTest.API_URL)
        # Make sure status code is 200
        self.assertEqual(r.status_code, 200)

    # POST request to /transactions with valid data returns 201
    def test_2_post_valid_transaction(self):
        r = requests.post(self.API_URL, json=ApiTest.TRANSACTION)
        # Make sure status code is 201
        self.assertEqual(r.status_code, 201)
        # Make sure the transaction is in the database

    # POST request to /transactions with valid data returns 201
    def test_3_put_valid_transaction_after_update(self):
        # POST a transaction
        requests.post(self.API_URL, json=ApiTest.TRANSACTION)
        # PUT the transaction
        r = requests.put(self.API_URL, json=ApiTest.POINTS)
        # Make sure status code is 201
        self.assertEqual(r.status_code, 200)
        # Check response for expected return data (list of transaction dictionaries)
        self.assertEqual(r.json(), ApiTest.NEW_TRANSACTION)