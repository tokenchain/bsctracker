from web3 import Web3, HTTPProvider
from eth_account import Account


BSC_API_1 = "https://bsc-mainnet.rpcfast.com?api_key=IeoliMrDIzyON5sNBVM04kGzox4uIWSMIarblgFZDLaDpiJb6SdUZIdNplG4cn1i"
"""
API collections
https://control.rpcfast.com/dashboard/?code=mLTkpMtxn1ggYFQkAjnuEwUV6pvd61JZwuuyGetjdjCi0&state=RnJZWmtJTFdaVi1YbDU0Q2o0RG5rQ2lQeEE2VVBkdFh1TEdYRkpIcWswSA%3D%3D
"""
BSC_API_2 = "https://bsc-dataseed.binance.org/"
BSC_API_3 = "https://bsc-dataseed1.defibit.io"


def write_func(contract_address, sender_address, private_key, signature):
    # Connect to Ethereum node
    web3 = Web3(HTTPProvider(BSC_API_1))

    # Set contract address and function signature
    # contract_address = '0x123456...'
    # signature = 'someFunction(uint256)'

    # Set function parameters
    param1 = 123
    """
    with perams.. 
    
  transaction = {
        'nonce': web3.eth.get_transaction_count(sender_address),
        'to': contract_address,
        'data': web3.sha3(signature.encode('utf-8'))[:4],
    }
    """
    # Create transaction

    transaction = {
        'nonce': web3.eth.getTransactionCount(sender_address),
        'to': contract_address,
        'data': web3.sha3(signature.encode('utf-8'))[:4] + web3.eth.encode_abi(['uint256'], [param1])
    }
    # Sign transaction with private key
    signed = Account.sign_transaction(transaction, private_key)

    # Send the raw transaction
    tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)

    # Wait for transaction to be confirmed
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)


def read_func(contract_address, signature, sender_address=None, private_key=None):
    # Connect to Ethereum node
    _web3 = Web3(HTTPProvider(BSC_API_2))

    print(_web3.eth.chain_id)
    # Get the output of the contract call
    output = _web3.eth.call({
        'to': contract_address,
        'data': _web3.keccak(text=signature)[:4],
    }, 'latest')
    # Decode the output of the contract call
    print(output)
    print("=========")
    result = output.hex()
    print("Result is: ", result)


def read_func_0x(contract_address, signature_code, sender_address=None, private_key=None):
    # Connect to Ethereum node
    _web3 = Web3(HTTPProvider(BSC_API_2))

    print(_web3.eth.chain_id)
    # Get the output of the contract call
    output = _web3.eth.call({
        'to': contract_address,
        'data': signature_code,
    }, 'latest')
    # Decode the output of the contract call
    result = output.hex()
    print("Result is: ", result)


def tx_get(tx_hash: str):
    # Connect to Ethereum node
    _web3 = Web3(HTTPProvider(BSC_API_2))
    by = _web3.eth.get_raw_transaction(tx_hash)
    result = by.hex()
    print(f"hex result: {result}")
