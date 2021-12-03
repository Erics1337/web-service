# Web Service
This API will allow you to access a simulated ecommerce back-end point system.

You can do things like:
 - [Add transactions](#add)
 - [Spend points](#spend)
 - [View list of payer point balance objects](#balances)
## Technologies used:
- Python
- Flask
- Flask Restful


# Getting Started
Make sure you have pipenv installed.
``` 
pip3 install pipenv 
```
Install project dependencies
```
pipenv install
```
Start the API flask_restful server
```
python3 api.py
```

# Examples
<a name="add"></a>Add transactions for a specific payer and date
```

```
<a name="spend"></a>Spend points using the rules above and return a list of {"payer": <string>, "points": <integer>} for each call
```
python3 api.py
```
<a name="balances"></a>Returns all payer points balances
```
python3 api.py
```

# Developer Notes
Users have points in their accounts
- Users see only a single balance
- For reporting purposes, points are tracked per payer/partner
  - Each transaction record contains a 
    - payer(string)
    - points(Integer)
    - timestamp(date)
- Rules for determining which points to spend first
  - Oldest points spent first
  - Do not want any payer's points to go negative

## Requirements:
- Routes for:
  - Adds transactions for a specific payer and date
  - Spend points using the rules above and return a list of {"payer": <string>, "points": <integer>} for each call
  - Returns all payer points balances

## Notes
- Do not need to use any durable data store; storing transactions in memory is acceptable

