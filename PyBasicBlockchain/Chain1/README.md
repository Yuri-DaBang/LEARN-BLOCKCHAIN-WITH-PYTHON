# PyBasicBlockchain Lib V1 🐍🧱

Welcome to **PyBasicBlockchain Lib V1**! Ever wondered how those magical digital coins work? Well, here's your chance to create your very own blockchain. Let's dive into the code, explained in the most hilarious way possible!

## Code Explained Line-by-Line

### Importing Libraries 📚

```python
import hashlib  # Hashing magic, like turning data into digital fingerprints! 🕵️‍♂️
import json  # Speaking in JSONish because it's the blockchain lingua franca! 🌐
from time import time  # Time flies when you're mining blocks! 🕒
from typing import List, Dict, Any, Optional  # Making Python understand our crazy types! 📋
```

### Block Class 💎
- The Block class represents a single block in the blockchain.
```python
class Block:
    def __init__(self, index: int, timestamp: float, transactions: List[Dict[str, Any]], previous_hash: str):
        self.index = index  # Where Mr. Block stands in the queue. 🏷️
        self.timestamp = timestamp  # When Mr. Block was born. ⏰
        self.transactions = transactions  # The juicy details (transactions) Mr. Block carries. 💸
        self.previous_hash = previous_hash  # The ID of Mr. Block's older sibling. 🧬
        self.nonce = 0  # Mr. Block's random number for mining tricks. 🎲
        self.hash = self.compute_hash()  # Mr. Block’s unique fingerprint. 🖐️

    def compute_hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True)  # Turn Mr. Block into a JSON string for hashing. 📜
        return hashlib.sha256(block_string.encode()).hexdigest()  # Hash the string like a blender on high speed. 🌀

    def mine_block(self, difficulty: int):
        required_prefix = '0' * difficulty  # The number of zeros Mr. Block needs to find. 🎯
        while not self.hash.startswith(required_prefix):  # Keep mining until Mr. Block gets lucky. 🍀
            self.nonce += 1  # Increment the nonce for each mining attempt. 🚀
            self.hash = self.compute_hash()  # Update Mr. Block’s fingerprint after each try. 🔄
```

### Blockchain Class 🏗️
- The Blockchain class manages the entire blockchain.
```python 
class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []  # The list where all Mr. Blocks hang out. 📚
        self.pending_transactions: List[Dict[str, Any]] = []  # Transactions waiting for a block party. 🎉
        self.difficulty = 4  # How tough the mining challenge is. 💪
        self.reward = 50  # Reward for mining a block. 💰
        self.create_genesis_block()  # The birth of the very first Mr. Block. 🌟

    def create_genesis_block(self):
        genesis_block = Block(0, time(), [], "0")  # The first block ever, with no transactions and no history. 👶
        self.chain.append(genesis_block)  # Add this ancient block to the chain. 📜

    def get_last_block(self) -> Block:
        return self.chain[-1]  # Find the most recent Mr. Block. 🔍

    def add_transaction(self, transaction: Dict[str, Any]):
        self.pending_transactions.append(transaction)  # Add a transaction to the waiting list. 📝

    def mine_pending_transactions(self, miner_address: str):
        new_block = Block(
            index=len(self.chain),  # The new block’s position in the chain. 🏷️
            timestamp=time(),  # The time the new block is created. ⏰
            transactions=self.pending_transactions + [{'sender': 'network', 'recipient': miner_address, 'amount': self.reward}],  # Transactions plus the mining reward. 💸
            previous_hash=self.get_last_block().hash  # The previous block’s hash. 🧬
        )
        new_block.mine_block(self.difficulty)  # Start mining until the block is worthy. ⛏️
        self.chain.append(new_block)  # Add this new block to the blockchain party. 🎉
        self.pending_transactions = []  # Clear the list of pending transactions. 🧹

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):  # Loop through each block starting from the second one. 🔁
            current_block = self.chain[i]  # The block we're currently checking. 🕵️‍♂️
            previous_block = self.chain[i - 1]  # The block just before the current one. 🧓

            if current_block.hash != current_block.compute_hash():  # Check if the block’s fingerprint hasn’t changed. ❓
                return False
            if current_block.previous_hash != previous_block.hash:  # Make sure the block’s previous hash matches the actual previous block. 🔗
                return False
        return True  # If everything checks out, the chain is valid! ✅

    def get_balance(self, address: str) -> int:
        balance = 0  # Start with zero balance. 🏦
        for block in self.chain:  # Loop through each block. 🔄
            for transaction in block.transactions:  # Loop through each transaction in the block. 🧾
                if transaction['sender'] == address:  # If this address is the sender, subtract the amount. ➖
                    balance -= transaction['amount']
                if transaction['recipient'] == address:  # If this address is the recipient, add the amount. ➕
                    balance += transaction['amount']
        return balance  # Return the final balance. 🏧
```

### Example Usage 🎉
- Let's see how we can use this awesome library!
```python
import PyBasicBlockchain  # Import the awesome PyBasicBlockchain library! 🚀

# Example usage
if __name__ == "__main__":
    blockchain = PyBasicBlockchain.Blockchain()  # Start a new blockchain. 🆕

    blockchain.add_transaction({"sender": "Alice", "recipient": "Bob", "amount": 50})  # Alice sends Bob 50 coins. 💸
    blockchain.add_transaction({"sender": "Bob", "recipient": "Charlie", "amount": 25})  # Bob sends Charlie 25 coins. 💸

    print("Mining pending transactions...")  # Announce the mining party. 🎉
    blockchain.mine_pending_transactions("Miner1")  # Mine those transactions into a new block. ⛏️

    blockchain.add_transaction({"sender": "Charlie", "recipient": "Dave", "amount": 10})  # Charlie sends Dave 10 coins. 💸

    print("Mining pending transactions...")  # Announce the mining party. 🎉
    blockchain.mine_pending_transactions("Miner1")  # Mine those transactions into a new block. ⛏️

    for block in blockchain.chain:  # Loop through each block and show off its details. 👀
        print(f"Block {block.index} - Hash: {block.hash} - Previous Hash: {block.previous_hash}")  # Print block index, hash, and previous hash. 🏷️
        print("Transactions:", block.transactions)  # Print block transactions. 💸
        print("Nonce:", block.nonce)  # Print block nonce. 🎲
        print()

    print("Is blockchain valid?", blockchain.is_chain_valid())  # Check and print if our blockchain is legit. ✅

    print("Balance of Miner1:", blockchain.get_balance("Miner1"))  # Print balance of Miner1. 💰
    print("Balance of Alice:", blockchain.get_balance("Alice"))  # Print balance of Alice. 💰
    print("Balance of Bob:", blockchain.get_balance("Bob"))  # Print balance of Bob. 💰
    print("Balance of Charlie:", blockchain.get_balance("Charlie"))  # Print balance of Charlie. 💰
    print("Balance of Dave:", blockchain.get_balance("Dave"))  # Print balance of Dave. 💰
```

## Customizing the Blockchain 🔧

### Adjusting the Difficulty 🎯
- You can change the mining difficulty by modifying the self.difficulty value in the Blockchain class:
```python
self.difficulty = 4  # Increase or decrease this value to make mining harder or easier.
```

### Setting the Mining Reward 💰
- You can change the mining reward by modifying the self.reward value in the Blockchain class:
```python
self.reward = 50  # Change this value to set a different reward for mining a block.
```

### Adding More Transactions 📝
- You can add as many transactions as you want before mining a block:
```python
blockchain.add_transaction({"sender": "Alice", "recipient": "Bob", "amount": 50})
blockchain.add_transaction({"sender": "Bob", "recipient": "Charlie", "amount": 25})
blockchain.add_transaction({"sender": "Charlie", "recipient": "Dave", "amount": 10})
# Add more transactions here...
```

### Modifying the Block Structure 🧱
- If you want to add more data to each block, you can modify the Block class:
```python
class Block:
    def __init__(self, index: int, timestamp: float, transactions: List[Dict[str, Any]], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.extra_data = "Extra data can be added here!"  # Add more fields as needed.
        self.hash = self.compute_hash()
```
- Remember to update the compute_hash method to include any new fields:
```python
def compute_hash(self) -> str:
    block_string = json.dumps(self.__dict__, sort_keys=True)
    return hashlib.sha256(block_string.encode()).hexdigest()
```
- With these customizations, you can tailor the blockchain to your specific needs. Have fun experimenting and learning about blockchain technology! 🚀💡

*FOR MORE INFO SEE `./KRAZY.md`*