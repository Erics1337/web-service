# Web Service

## Background
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

## Web Service Requirements:
- Routes for:
  - Adds transactions for a specific payer and date
  - Spend points using the rules above and return a list of {"payer": <string>, "points": <integer>} for each call
  - Returns all payer points balances

## Notes
- Must come up with specifics of requests/responses
- Do not need to use any durable data store; storing transactions in memory is acceptable

