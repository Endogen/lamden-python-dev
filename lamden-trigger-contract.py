import time
import json
import requests

from lamden.crypto.transaction import build_transaction
from lamden.crypto.wallet import Wallet

# Wallet address
address = "77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686"
# Wallet private key
privkey = "01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9"

# Get nonce for our address
url = "https://testnet-master-1.lamden.io"
nonce = requests.get(f"{url}/nonce/{address}")
nonce = json.loads(nonce.text)

# Build transaction
tx = build_transaction(
    wallet=Wallet(privkey),
    processor=nonce["processor"],
    stamps=100,
    nonce=nonce["nonce"],
    contract="con_dice",
    function="roll",
    kwargs={}
)

# Send transaction
dice_roll = requests.post(url, data=tx)
tx_hash = json.loads(dice_roll.text)
tx_hash = tx_hash["hash"]

# Wait to make sure that transaction is already processed
time.sleep(1)

# Get transaction details for given tx hash
result = requests.get(f"{url}/tx?hash={tx_hash}")
result = json.loads(result.text)
result = result["result"]
print("dice - roll", result)

# Example Output
# dice - roll 6