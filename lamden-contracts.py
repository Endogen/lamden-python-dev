# Wrap contract methods in parent method 'greeting()' 
# so that we are able to reference the contract
def greeting():
    @export
    def hello():
        return 'Hello World!'

    @export
    def add(a: int, b: int):
        return private_add(a, b)

    def private_add(a, b):
        return a + b

from contracting.client import ContractingClient

# Client to interact with local contracts
client = ContractingClient()

# Submit contract locally
client.submit(greeting)

# List all locally available contracts
print("contracts", client.get_contracts())

# Retrieve local contract
greeting = client.get_contract("greeting")

# Execute contract method 'hello()'
print("greeting - hello()", greeting.hello())
# Execute contract method 'add()'
print("greeting - add()", greeting.add(a=1, b=3))

# Output
# contracts ['submission', 'greeting']
# greeting - hello() Hello World!
# greeting - add() 4