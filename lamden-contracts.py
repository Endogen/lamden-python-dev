from contracting.client import ContractingClient
client = ContractingClient()

def greeting():
    @export
    def hello():
        return 'World!'

    @export
    def add(a: int, b: int):
        return private_add(a, b)

    def private_add(a, b):
        return a + b

def split_send():
	@export
	def send(addresses: Array, total_amount: float):
		single_amount = total_amount / len(addresses)
		print("single_amount", single_amount)

		for address in addresses:
			currency.transfer_from(amount = single_amount, to=address, main_account=ctx.signer)

def dice():
	@export
	def roll():
		# TODO: Use hash function somehow
		pass

client.submit(split_send)
print(client.get_contracts())

split_send = client.get_contract("split_send")

addresses = []

print(split_send(addresses, 10))