from web3 import Web3

# Connect to Ganache
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

if web3.is_connected():
    print("Connected to Ganache")
else:
    print("Failed to connect to Ganache")

# Replace these with your details from Ganache
sender_address = '0xYourSenderAddress'
receiver_address = '0xYourReceiverAddress'
private_key = 'YourPrivateKey'

# Get the nonce (transaction count for the sender address)
nonce = web3.eth.get_transaction_count(sender_address)

# Create the transaction dictionary
tx = {
    'nonce': nonce,
    'to': receiver_address,
    'value': web3.to_wei(1, 'ether'),  # Amount to send in wei
    'gas': 21000,  # Gas limit for a standard ETH transfer
    'gasPrice': web3.to_wei('20', 'gwei'),  # Gas price in gwei
}

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Get the transaction hash
print(f'Transaction sent with hash: {web3.to_hex(tx_hash)}')