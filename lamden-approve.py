import json
import time
import requests

from lamden.crypto.transaction import build_transaction
from lamden.crypto.wallet import Wallet

# Private key to send TAU from
privkey = "01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9"

# Generate wallet to send TAU from
wallet = Wallet(privkey)

# Public address to send TAU from
address = wallet.verifying_key

# Amount of TAU to send
amount = 10

# Maternode URL (testnet)
url = "https://testnet-master-1.lamden.io"

# Get nonce for our address
nonce = requests.get(f"{url}/nonce/{address}")
nonce = json.loads(nonce.text)

# List of addresses to send TAU to
addresses = [
	"b0bb69bb8722e0b3364ada9d1d96675e8025f552e7d03770618c43b7df0584a5",
	"523e4db1ad94e8c70d63b788b4a4356e5fd9f026b3f1b16e115386fdb70ffb4d"
]

# Build transaction to trigger 'con_multisend' contract
tx = build_transaction(
    wallet=wallet,
    processor=nonce["processor"],
    stamps=500,
    nonce=nonce["nonce"],
    contract="con_multisend",
    function="send",
    kwargs={"addresses": addresses, "amount": amount}
)

# Send transaction
result = requests.post(url, data=tx)
print("con_multisend", result.text)

# Output
# con_multisend {"success":"Transaction successfully submitted to the network.","hash":"204dfa36128376621b4887b2da05d805bcd2ad284768ccf7c8102245fcd4dc39"}

tx_hash = json.loads(result.text)
tx_hash = tx_hash["hash"]

# Wait to make sure that transaction is already processed
time.sleep(1)

# Get transaction details for given tx hash
error = requests.get(f"{url}/tx?hash={tx_hash}")
error = json.loads(error.text)
error = error["result"]
print("error", error)

# Output
# error AssertionError('Not enough coins approved to send! You have 0.0 and are trying to spend 10',)

# Get new nonce for our address
nonce = requests.get(f"{url}/nonce/{address}")
nonce = json.loads(nonce.text)

# Build transaction to approve contract to spend TAU
# We need to approve double the amount since we want to send 10 TAU to each address
tx = build_transaction(
    wallet=wallet,
    processor=nonce["processor"],
    stamps=500,
    nonce=nonce["nonce"],
    contract="currency",
    function="approve",
    kwargs={"amount": float(amount * 2), "to": "con_multisend"}
)

# Send transaction
approve = requests.post(url, data=tx)
print("approve", approve.text)

# Output
# approve {"success":"Transaction successfully submitted to the network.","hash":"e3debf48c179fb96ca0f1902b348ef675d488300525a9dc7c740911f8a5aeaff"}

# Wait to make sure that transaction is already processed
time.sleep(1)

# Get amount of TAU that is approved to be spent by the smart contract
key = f"{wallet.verifying_key}:con_multisend"
verify = requests.get(f"{url}/contracts/currency/balances?key={key}")
print("verify", verify.text)

# Output
# verify {"value":{"__fixed__":"20.0"}}

# Get new nonce for our address
nonce = requests.get(f"{url}/nonce/{address}")
nonce = json.loads(nonce.text)

# Build transaction to trigger 'con_multisend' contract again
# Now the transaction should go through since we approved the amount and contract
tx = build_transaction(
    wallet=wallet,
    processor=nonce["processor"],
    stamps=500,
    nonce=nonce["nonce"],
    contract="con_multisend",
    function="send",
    kwargs={"addresses": addresses, "amount": amount}
)

# Send transaction
result = requests.post(url, data=tx)
print("con_multisend", result.text)

# Output
# con_multisend {"success":"Transaction successfully submitted to the network.","hash":"66ffc0ffc5427ae2fb7b7a57137490f1ec1ace54071c1dd71e5a476d427a2079"}

tx_hash = json.loads(result.text)
tx_hash = tx_hash["hash"]

# Wait to make sure that transaction is already processed
time.sleep(1)

# Get transaction details for given tx hash
# If 'result' is 'None' then we didn't get any error back
result = requests.get(f"{url}/tx?hash={tx_hash}")
result = json.loads(result.text)
status_data = result["status"]
result_data = result["result"]
print("status_data", status_data)
print("result_data", result_data)

# Output
# status_data 0
# result_data None