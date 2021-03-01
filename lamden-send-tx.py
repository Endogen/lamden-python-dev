import json
import requests

from lamden.crypto.transaction import build_transaction
from lamden.crypto.wallet import Wallet

# Wallet address
address = "77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686"
# Wallet private key
privkey = "01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9"

# Receiving address
to_address = "2f3d50e4528e196233617645f85c76b4c6256f307ef3c3213aabe5a6ce956900"
# Amount of TAU to send
amount = 1

# URL to get nonce for our address
url = "https://testnet-master-1.lamden.io"

nonce = requests.get(f"{url}/nonce/{address}")
nonce = json.loads(nonce.text)

# Create new wallet
wallet = Wallet(privkey)

# Build transaction
tx_data = build_transaction(
    wallet=wallet,
    processor=nonce["processor"],
    stamps=100,
    nonce=nonce["nonce"],
    contract="currency",
    function="transfer",
    kwargs={"amount": amount, "to": to_address}
)

# Send transaction
tx = requests.post(url, data=tx_data)
tx = json.loads(tx.text)
print("tx", tx)

# Get transaction hash
tx_hash = tx["hash"]
print("hash", tx_hash)

# Output
# tx {'success': 'Transaction successfully submitted to the network.', 'hash': '002c078784ccc8d273fab654f3586087c4a7b23a9745b2181d874078b4204c7f'}
# tx_hash 002c078784ccc8d273fab654f3586087c4a7b23a9745b2181d874078b4204c7f