import nacl.signing
import secrets

seed = secrets.token_bytes(32)

# Signing key
sk = nacl.signing.SigningKey(seed=seed)

# Verifying key
vk = sk.verify_key

# User friendly representation of keys
address = vk.encode().hex()
privkey = sk.encode().hex()

print("address", address)
print("privkey", privkey)

# Example output
# address 77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686
# privkey 01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9

seed = bytes.fromhex(privkey)

sk = nacl.signing.SigningKey(seed=seed)
vk = sk.verify_key

print("address", address)
print("privkey", privkey)