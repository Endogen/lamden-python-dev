import requests
import json

# Maternode URL (testnet)
url = "https://testnet-master-1.lamden.io"

# Transaction hash from triggering a smart contract
tx_hash = "66ffc0ffc5427ae2fb7b7a57137490f1ec1ace54071c1dd71e5a476d427a2079"

# Get transaction details for given tx hash
result = requests.get(f"{url}/tx?hash={tx_hash}")
result = json.loads(result.text)
print("result", result)

# Output
# {'hash': '66ffc0ffc5427ae2fb7b7a57137490f1ec1ace54071c1dd71e5a476d427a2079', 'result': 'None', 'stamps_used': 32, 'state': [{'key': 'currency.balances:77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686:con_multisend', 'value': {'__fixed__': '0.0'}}, {'key': 'currency.balances:77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686', 'value': {'__fixed__': '417.8461538461538465'}}, {'key': 'currency.balances:b0bb69bb8722e0b3364ada9d1d96675e8025f552e7d03770618c43b7df0584a5', 'value': 40}, {'key': 'currency.balances:523e4db1ad94e8c70d63b788b4a4356e5fd9f026b3f1b16e115386fdb70ffb4d', 'value': 30}], 'status': 0, 'transaction': {'metadata': {'signature': '13f216bdcafbb3101ce52c1306d6ed6ee848901980426ad6e5e166d61838575cc23951dae33c80da799f365ec534efc98c9f1197ada74f2606284c2e647eb701', 'timestamp': 1614641383}, 'payload': {'contract': 'con_multisend', 'function': 'send', 'kwargs': {'addresses': ['b0bb69bb8722e0b3364ada9d1d96675e8025f552e7d03770618c43b7df0584a5', '523e4db1ad94e8c70d63b788b4a4356e5fd9f026b3f1b16e115386fdb70ffb4d'], 'amount': 10}, 'nonce': 30, 'processor': '89f67bb871351a1629d66676e4bd92bbacb23bd0649b890542ef98f1b664a497', 'sender': '77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686', 'stamps_supplied': 500}}}

# We need to check the value of 'status' to know if a transaction went through
status = result["status"]
print("status", status)

# Output
# status 0