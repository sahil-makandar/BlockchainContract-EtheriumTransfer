# Ethereum Transaction Script Using Web3.py and Ganache

This repository contains a Python script to send Ether (ETH) from one address to another using the Web3.py library and Ganache for local Ethereum blockchain simulation.

## Prerequisites

Before you start, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Ganache](https://trufflesuite.com/ganache/)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/sahil-makandar/BlockchainContract-EtheriumTransfer.git
    cd BlockchainContract-EtheriumTransfer
    ```

2. **Install the required Python packages**:
    ```sh
    pip install web3
    ```

3. **Download and install Ganache**:
    - Go to the [Ganache website](https://trufflesuite.com/ganache/).
    - Download the version suitable for your operating system.
    - Install and run Ganache. Note the RPC server URL (usually `http://127.0.0.1:7545`) and the generated accounts with their private keys.

## Configuration

1. **Replace the placeholder values in `send_eth_ganache.py`** with your actual details from Ganache:

    ```python
    sender_address = '0xYourSenderAddress'
    receiver_address = '0xYourReceiverAddress'
    private_key = 'YourPrivateKey'  # Do not share your private key
    ```

2. Save your changes.

## Running the Script

1. **Run the script**:
    ```sh
    python send_eth_ganache.py
    ```

2. **Check Ganache**: 
   - Open Ganache and verify that the transaction has been processed and the balances have been updated accordingly.

## How the Script works

The script performs the following steps:

1. **Connect to Ganache**:
    ```python
    ganache_url = 'http://127.0.0.1:7545'
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    if web3.is_connected():
        print("Connected to Ganache")
    else:
        print("Failed to connect to Ganache")
    ```

2. **Set up transaction details**:
    - The sender address, receiver address, and sender's private key are obtained from Ganache.
    - The nonce (transaction count) is fetched for the sender address.
    - The transaction dictionary is created, specifying the receiver address, amount to send (in wei), gas limit, and gas price.

    ```python
    nonce = web3.eth.get_transaction_count(sender_address)

    tx = {
        'nonce': nonce,
        'to': receiver_address,
        'value': web3.to_wei(1, 'ether'),  # Amount to send in wei
        'gas': 21000,  # Gas limit for a standard ETH transfer
        'gasPrice': web3.to_wei('20', 'gwei'),  # Gas price in gwei
    }
    ```

3. **Sign and send the transaction**:
    - The transaction is signed using the sender's private key.
    - The signed transaction is sent to the network.
    - The transaction hash is printed to confirm that the transaction has been sent.

    ```python
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f'Transaction sent with hash: {web3.to_hex(tx_hash)}')
    ```
