from lamden.crypto.wallet import Wallet, verify

privkey = "01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9"

wallet = Wallet(privkey)

# Let's sign this message and receive a signature
message = "Some random string"
signature = wallet.sign(message)

print("signature", signature)

# Output
# ba32fcfa1b975f1572a1be21efa949d29f3a9e15e064d0e8d5f90eff596a204dd20ad8ca53161224ff62e97c147aba297f9ba8fd3a1eb8223c095cf6bcc85409

# Let's verify that the message was signed by my public address
signature = "ba32fcfa1b975f1572a1be21efa949d29f3a9e15e064d0e8d5f90eff596a204dd20ad8ca53161224ff62e97c147aba297f9ba8fd3a1eb8223c095cf6bcc85409"
was_it_me = verify(wallet.verifying_key, message, signature)

print("was_it_me", was_it_me)

# Output
# was_it_me True