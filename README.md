# Lamden for Python Developers

Guide for Python developers to get started fast on Lamden

---

[Lamden](https://lamden.io) is a perfomant Blockchain built on Python that is specifically targeting Python developers. It's heavily build on smart contracts, transactions are super fast an it's easy to interact with. This short guide is meant to get you started even fasted on getting things done with Lamden.

But first of all, why should you care? There are countless other blockchains out there, right? Well, let's see:

- In general, it's a solid custom blockchain project with a nice community and interesting tokenomics
  
- Always wanted to code smart contracts but Solidity just isn't your thing? On Lamden you code and deploy smart contracts with Python - directly from your browser wallet
  
- Core developers pay a bounty of \$400 (\$200 via PayPal and \$200 $ worth of TAU the native coin) to everyone that codes up with a smart contract that is somewhat userfull
  
- Once you created a smart contract you receive 90% of all transaction fees that are processed through that smart contract
  

## Prerequisites

### Python

Make sure to have Python 3 installed (i would recommand to use Python 3.9) alongside `python3-dev` so that you are able to build Python extensions. To install it:

##### macOS

If you don't already have it install the [Homebrew](https://docs.brew.sh/Installation) package manager and then install Python:

```shell
brew install python@3.9
```

That should install everything you need

##### Linux

Add the deadsnakes PPA to your system’s sources list:

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
```

Then install Python 3.9:

```shell
sudo apt-get install python3.9 python3.9-dev
```

##### Windows

Download and install Python 3.9 from [here](https://www.python.org/downloads/windows)

### MongoDB

You will need to install MongoDB to be able to interact with Lamden via the `lamden` module or `contracting` module. It's a hard requirement that you can't circumvent.

Please consult the [Mongo DB Docs](https://docs.mongodb.com/manual/administration/install-community) for instructions on how to install it on the different operating systems. After you've installed it, authentication is disabled per default and that's exactly what we need so please don't change that.

## Interact with Lamden

In general it's a good idea to check out the [Lamden GitHub](https://github.com/Lamden) but that can also be a bit confusing since there are quite a few Python repositories there and it's not always immediately clear what they do or if you need them to be able to start coding on Lamden.

Here's a short overview of the Python code that you should have heard about:

- [lamden](https://github.com/Lamden/lamden) - The Lamden node
  
  - **Important for development**
    
  - Includes code to create wallets and send transactions
    
  - You don't need to run your own node
    
  - Installable via `pip`
    
- [contracting](https://github.com/Lamden/contracting) - Interact with smart contracts
  
  - **Important for development**
    
  - Installable via `pip`
    
- [cilantro-enterprise](https://github.com/Lamden/cilantro-enterprise) - The (old) Lamden node
  
  - **Outdated! Don't use**
- [clove](https://github.com/Lamden/clove) - Exchange crypto via atomic swaps
  
  - Not needed for basic use cases
    
  - Installable via `pip`
    
- [flora](https://github.com/Lamden/flora) - Distributed smart contract package manager
  
  - Not needed for development
    
  - Installable via `pip`
    
- [lampy](https://github.com/Lamden/lampy) - Lamden Python Client
  
  - **Outdated! Don't use**
    
  - You can check it out to get an idea how things work
    
- [smart_contracts](https://github.com/Lamden/smart_contracts) - Example smart contracts on Lamden
  
  - Check the examples if you want to create your own smart contract
- [lamden_things](https://github.com/Lamden/lamden_things) - Example smart contracts for NFTs on Lamden
  
  - Check the examples if you want to create your own NFT tokens

### Generate key pair

The Lamden protocol uses [ED25519](https://ed25519.cr.yp.to/) for cryptographic keys and the [PyNaCl](https://pynacl.readthedocs.io/en/stable/) library for the specific Python bindings of the original C code. If you just want to be able to generate valid key pairs then it's enough to install the `pynacl`module:

```shell
pip3 install pynacl
```

That is relatively low-level and probalby not what you will end up using but generating an address (verifying key) and a private key (signing key) would look like this:

```python
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
```

If you already have a hex private key and you want to generate the seed to get the corresponding address or sign a message or something like that:

```python
seed = bytes.fromhex(seed)
```

You can then pass the `seed` as an argument to `SigningKey` again

### Lamden wallet

Of course Lamden has all the low-level wallet stuff including signing and verifying messages already bundled in their own `lamden` module which represents the blockchain node. You can install it with:

```shell
pip3 install lamden
```

But you need to be aware that **you will need to install MongoDB to be able to successfully install `lamden`**. No way around that.

#### Wallet creation

To instanciate a wallet:

```python
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
```

If you already have a private key that you want to use to instantiate your wallet, pass it as the `seed` argument to `Wallet`:

```python
from lamden.crypto.wallet import Wallet

privkey = "01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9"

# Create a wallet based on the given private key
wallet = Wallet(privkey)

# Wallet address
address = wallet.verifying_key

print("address", address)

# Output
# address 77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686
```

#### Signing & verifying

Once you have a `Wallet` instance you can sign and verify messages:

```python
from lamden.crypto.wallet import Wallet, verify

privkey = "01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9"

wallet = Wallet(privkey)

# Let's sign this message and receive a signature
message = "Some random string"
signature = wallet.sign(message)

print("signature", signature)

# Output
# signature ba32fcfa1b975f1572a1be21efa949d29f3a9e15e064d0e8d5f90eff596a204dd20ad8ca53161224ff62e97c147aba297f9ba8fd3a1eb8223c095cf6bcc85409

# Let's verify that the message was signed by my public address
signature = "ba32fcfa1b975f1572a1be21efa949d29f3a9e15e064d0e8d5f90eff596a204dd20ad8ca53161224ff62e97c147aba297f9ba8fd3a1eb8223c095cf6bcc85409"
was_it_me = verify(wallet.verifying_key, message, signature)

print("was_it_me", was_it_me)

# Output
# was_it_me True
```

#### Sending transaction

The next step could be to send a transaction. But before we can actually do that we need to get a [nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) from the node that will process our transaction.

##### Get a nonce

So how do we get a nonce? First of all we need to know how to communcate with a node on the network. We need some masternode address:

**Mainnet Masternode**

```
https://masternode-01.lamden.io
```

**Testnet Masternode**

```
https://testnet-master-1.lamden.io
```

Next we need to understand how to communicate with the node. There is a [REST API](https://docs.lamden.io/docs/develop/blockchain/masternode_api) that we can use. Specifically the ["get transaction nonce" route](https://docs.lamden.io/docs/develop/blockchain/masternode_api#get-transaction-nonce). We can call the following URL in a browser to get a nonce for our public address:

```
https://masternode-01.lamden.io/nonce/77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686
```

This is the JSON reply we get:

```json
{
    "nonce": 0,
    "processor": "5b09493df6c18d17cc883ebce54fcb1f5afbd507533417fe32c006009a9c3c4a",
    "sender": "77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686"
}
```

The `processor` is the public address (verifying key) of the node, `sender` is our own public address and `nonce` is the transaction counter for our address.

##### Stamps

We will also need to define how much [stamps](https://contracting.lamden.io/concepts/stamps) we want to use (which is basically a way to determine the fee that needs to be payed in order to be able to send a transaction). A generally good value for `stamps` is `100`.

Stamps are converted to TAU (the native coin on the Landom blockchain) automatically based on the type of operation that needs to be done by the node and that is defined in the transaction.

##### Contract & function

Since Lamden is heavily based on smart contracts, every transaction that is being sent triggers a smart contract. Even a "normal" transfer of the native TAU coin executes a smart contract.

And since that is the case, we also need to specify the contract name and the function name withing that contract that needs to be executed with our transaction.

For a normal transfer of TAU coins the contract name is `currency` and the function name is `transfer`.

##### Sending

Now that we have all the details we can finally send the transaction via [REST API](https://docs.lamden.io/docs/develop/blockchain/masternode_api#post-transaction) but please note that it's important that the node that sent us the nonce is also the one that will process the transaction:

```python
import requests

from lamden.crypto.transaction import build_transaction
from lamden.crypto.wallet import Wallet

# Wallet address
address = "77b9c48aa5e43d5bff575140f484bbda55ad2a619160b5eb5c04d8f27f437686"
# Wallet private key
privkey = "01c4763eadd4285cc31fdd60dedb4fa7c68f29e325775dc7f7f082bbab9b5fc9"

# URL to get nonce for our address
url = f"https://masternode-01.lamden.io/nonce/{address}"

nonce = requests.get(url)

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

# Get transaction hash
tx_hash = tx["hash"]
```

### Smart contracts

As already said previously, Lamden is heavily based on smart contracts and thus every transaction executes a smart contract. You can get a list of all available smart contracts by calling this [REST API](https://docs.lamden.io/docs/develop/blockchain/masternode_api/#get-contracts).

To be able to interact with smart contracts you will need to install the `contracting` module:

```shell
pip3 install contracting
```

#### Coding

You can code up a smart contract directly in your [Chrome wallet](https://chrome.google.com/webstore/detail/lamden-wallet-browser-ext/fhfffofbcgbjjojdnpcfompojdjjhdim) and also test it there for basic correctness.

#### Testing

#### Deploying

Deploy Smart Contracts with:

```python
from contracting.client import ContractingClient
```