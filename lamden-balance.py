import requests

from lamden.crypto.wallet import Wallet
from contracting.db.encoder import decode

def get_balance(address):
	# Explorer URL
	url = "https://masternode-01.lamden.io"

	# Get balance for a given address
	res = requests.get(f"{url}/contracts/currency/balances?key={address}")
	return res.text

# Private key of wallet with balance
privkey = "17790cb73293eb1b46ac3e10bc3a62fe6826404d32635c0cfee6893d3e6a7aed"

# Create a wallet for the given privkey
wallet = Wallet(privkey)

# Wallet address
address = wallet.verifying_key

# Let's get the balance of that address
balance = get_balance(address)
print("balance", balance)
print("balance", decode(balance))

# Output
# balance {"value":{"__fixed__":"125.35"}}
# balance {'value': Decimal('125.35')}