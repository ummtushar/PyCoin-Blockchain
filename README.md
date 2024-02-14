# PyCoin-Blockchain
Building a blockchain purely on python

# Creating a transaction
Run the following in the terminal:

```
curl "localhost:5000/txion" \
     -H "Content-Type: application/json" \
     -d '{"from": "akjflw", "to":"fjlakdj", "amount": 3}'
```
# Mining a new block

```
curl localhost:5000/mine
```
All creds to: @aunyks
