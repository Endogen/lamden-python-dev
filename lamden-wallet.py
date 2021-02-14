from lamden.crypto.wallet import Wallet

# Create a new wallet with a new key pair
wallet = Wallet()

# Wallet address
address = wallet.verifying_key

# Wallet private key
privkey = wallet.signing_key

print("address", address)
print("privkey", privkey)

# Example output
# address 77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686
# privkey 01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9