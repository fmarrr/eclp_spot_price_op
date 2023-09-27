import os
from dotenv import load_dotenv
from web3 import Web3
import json

# Connect to Infura
load_dotenv()
infura_provider = Web3.HTTPProvider("https://optimism-mainnet.infura.io/v3/5422ebc991684c9ebc64ff6a1c5938dc")
w3 = Web3(infura_provider)

# Initialize contract
contract_address = "0xBA12222222228d8Ba445958a75a0704d566BF2C8"

# Load the queryBatchSwap ABI from the JSON file
with open('/Users/flora/PycharmProjects/pythonProject/balancer_queryBatchSwap.json', 'r') as query_batch_swap_abi_file:
    query_batch_swap_abi = json.load(query_batch_swap_abi_file)

# Create a contract instance
contract = w3.eth.contract(address=contract_address, abi=query_batch_swap_abi)


# Function to simulate queryBatchSwap
def simulate_query_batch_swap():
    # Arguments for queryBatchSwap
    kind = 0 # uint8
    # Array of tuples for swaps
    # Each tuple contains:
    # (bytes32, uint256, uint256, uint256, bytes)
    swaps = [
        (
            bytes.fromhex('7ca75bdea9dede97f8b13c6641b768650cb837820002000000000000000000d5'),  # bytes32 (eclp poolID)
            0,  # uint256 (0 for WETH)
            1000000000000000000,  # uint256 (1 for wstETH)
            1000000000000,  # uint256 (example amount)
            b'example_bytes'  # bytes (example)
        )
    ]

    # Array of addresses (tokens)
    # This array should contain the token addresses for your swap
    address = [
        "0x4200000000000000000000000000000000000006",  # WETH
        "0x1F32b1c2345538c0c6f582fCB022739c4A194Ebb"  # wstETH
    ]

    # Tuple for funds
    funds = (
        "0x0000000000000000000000000000000000000000",  # Replace with the user's address
        False,
        "0x0000000000000000000000000000000000000000",  # Replace with the recipient's address
        False
    )

    # Encode the function call manually
    function_data = contract.encodeABI(
        fn_name="queryBatchSwap",
        args=[kind, swaps, address, funds]
    )

    # Simulate the transaction using eth_call
    result = w3.eth.call({
        'to': contract_address,
        'data': function_data,
    })

    # Print or process the result
    print(f"Simulated queryBatchSwap result: {result}")


if __name__ == "__main__":
    simulate_query_batch_swap()
