# PyBasicBlockchain2 Lib V1 📩🧱

Welcome to **PyBasicBlockchain2 Lib V1**! Ever wanted to build your own messaging blockchain? Now you can! Let's dive into the code, explained in the most hilarious way possible!

## Code Explained Line-by-Line

### Importing Libraries 📚

```python
import hashlib  # Turning data into digital fingerprints! 🕵️‍♂️
import json  # Speaking in JSONish, the blockchain lingua franca! 🌐
from time import time  # Time flies when you're mining blocks! 🕒
from typing import List, Dict, Any  # Making Python understand our crazy types! 📋
```

### MessageBlock Class 💎
- The MessageBlock class represents a single block in the messaging blockchain.
```python
class MessageBlock:
    def __init__(self, index: int, timestamp: float, messages: List[Dict[str, Any]], previous_hash: str):
        self.index = index  # Where Mr. Block stands in the queue. 🏷️
        self.timestamp = timestamp  # When Mr. Block was born. ⏰
        self.messages = messages  # The juicy details (messages) Mr. Block carries. 💬
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

### MessagingBlockchain Class 🏗️
- The MessagingBlockchain class manages the entire messaging blockchain.
```python
class MessagingBlockchain:
    def __init__(self):
        self.chain: List[MessageBlock] = []  # The list where all Mr. Blocks hang out. 📚
        self.pending_messages: List[Dict[str, Any]] = []  # Messages waiting for a block party. 🎉
        self.difficulty = 4  # How tough the mining challenge is. 💪
        self.mining_reward = 1  # Reward for mining a block. 💰
        self.create_genesis_block()  # The birth of the very first Mr. Block. 🌟

    def create_genesis_block(self):
        genesis_block = MessageBlock(0, time(), [], "0")  # The first block ever, with no messages and no history. 👶
        genesis_block.mine_block(self.difficulty)  # Mine the genesis block. ⛏️
        self.chain.append(genesis_block)  # Add this ancient block to the chain. 📜

    def get_last_block(self) -> MessageBlock:
        return self.chain[-1]  # Find the most recent Mr. Block. 🔍

    def add_message(self, message: Dict[str, Any]):
        self.pending_messages.append(message)  # Add a message to the waiting list. 📝

    def mine_pending_messages(self, miner_address: str):
        self.pending_messages.append({
            "sender": "Network",
            "recipient": miner_address,
            "content": f"Mining reward: {self.mining_reward}",
            "timestamp": time()
        })
        new_block = MessageBlock(
            index=len(self.chain),  # The new block’s position in the chain. 🏷️
            timestamp=time(),  # The time the new block is created. ⏰
            messages=self.pending_messages.copy(),  # Messages plus the mining reward. 💬
            previous_hash=self.get_last_block().hash  # The previous block’s hash. 🧬
        )
        new_block.mine_block(self.difficulty)  # Start mining until the block is worthy. ⛏️
        self.chain.append(new_block)  # Add this new block to the blockchain party. 🎉
        self.pending_messages = []  # Clear the list of pending messages. 🧹

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):  # Loop through each block starting from the second one. 🔁
            current_block = self.chain[i]  # The block we're currently checking. 🕵️‍♂️
            previous_block = self.chain[i - 1]  # The block just before the current one. 🧓

            if current_block.hash != current_block.compute_hash():  # Check if the block’s fingerprint hasn’t changed. ❓
                print(f"Block {current_block.index} hash mismatch: {current_block.hash} != {current_block.compute_hash()}")
                return False
            if current_block.previous_hash != previous_block.hash:  # Make sure the block’s previous hash matches the actual previous block. 🔗
                print(f"Block {current_block.index} previous hash mismatch: {current_block.previous_hash} != {previous_block.hash}")
                return False
        return True  # If everything checks out, the chain is valid! ✅

    def get_user_messages(self, user_address: str) -> List[Dict[str, Any]]:
        user_messages = []  # List to store messages for the user. 📩
        for block in self.chain:  # Loop through each block. 🔄
            for message in block.messages:  # Loop through each message in the block. 🧾
                if message['recipient'] == user_address:  # If this address is the recipient, add the message. ➕
                    user_messages.append(message)
        return user_messages  # Return the list of user messages. 🏧

    def get_sent_messages(self, user_address: str) -> List[Dict[str, Any]]:
        sent_messages = []  # List to store sent messages. 📤
        for block in self.chain:  # Loop through each block. 🔄
            for message in block.messages:  # Loop through each message in the block. 🧾
                if message['sender'] == user_address:  # If this address is the sender, add the message. ➕
                    sent_messages.append(message)
        return sent_messages  # Return the list of sent messages. 📦

    def get_user_history(self, user_address: str) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "received": self.get_user_messages(user_address),  # Get received messages. 📨
            "sent": self.get_sent_messages(user_address)  # Get sent messages. 📤
        }
```

## Example Usage 🎉
- Let's see how we can use this awesome library!
```python
import PyBasicBlockchain2
from time import time

if __name__ == "__main__":
    messaging_blockchain = PyBasicBlockchain2.MessagingBlockchain()  # Create a new blockchain 🆕

    # Add some messages 📩
    messaging_blockchain.add_message({"sender": "Alice", "recipient": "Bob", "content": "Hello, Bob!", "timestamp": time()})
    messaging_blockchain.add_message({"sender": "Bob", "recipient": "Alice", "content": "Hi, Alice!", "timestamp": time()})

    print("Mining pending messages...⛏️")
    messaging_blockchain.mine_pending_messages("Miner1")  # Mine those messages! 🤑

    # Add more messages 📩
    messaging_blockchain.add_message({"sender": "Charlie", "recipient": "Dave", "content": "Hey Dave, long time no see!", "timestamp": time()})
    messaging_blockchain.add_message({"sender": "Dave", "recipient": "Charlie", "content": "Hey Charlie, indeed! How have you been?", "timestamp": time()})

    print("Mining pending messages...⛏️")
    messaging_blockchain.mine_pending_messages("Miner2")  # Another round of mining! 💰

    # Print the details of each block in the chain 🧱
    for block in messaging_blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash} - Previous Hash: {block.previous_hash}")
        print("Messages:", block.messages)
        print("Nonce:", block.nonce)
        print()

    # Check if the blockchain is still valid ✅
    print("Is blockchain valid?", messaging_blockchain.is_chain_valid())

    # Get messages for a specific user 🕵️‍♂️
    print("Messages for Bob:", messaging_blockchain.get_user_messages("Bob"))
    print("Messages for Alice:", messaging_blockchain.get_user_messages("Alice"))
    print("Messages for Dave:", messaging_blockchain.get_user_messages("Dave"))

    # Get the entire message history for a user 🕵️‍♀️
    print("Message history for Charlie:", messaging_blockchain.get_user_history("Charlie"))
```

## Customizing Your Blockchain Adventure 🔧

### Adjust the Mining Difficulty 🎯
- Change the self.difficulty value in the MessagingBlockchain class to make mining easier or harder. More zeros = tougher mining!
```python
self.difficulty = 4  # Increase or decrease this value to adjust mining difficulty.
```

### Modify the Mining Reward 💰
- Update the self.mining_reward value to set a different reward for mining a block.
```python
self.mining_reward = 1  # Change this value to set a different mining reward.
```

### Customize the Block Structure 🧱
- If you want to add more data to each block, modify the MessageBlock class.
```python
class MessageBlock:
    def __init__(self, index: int, timestamp: float, messages: List[Dict[str, Any]], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.messages = messages
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

### Add New Features or Methods 🛠️
- Extend the MessagingBlockchain class with new features or methods to enhance functionality, such as advanced message filtering or analytics.
```python
class MessagingBlockchain:
    # Existing methods...

    def get_message_count(self) -> int:
        count = 0
        for block in self.chain:
            count += len(block.messages)
        return count  # Return the total number of messages in the blockchain.
```

## Example Code: Adjusting Difficulty and Reward 🎉
- Here's how to use the customized blockchain features in practice:
```python
import PyBasicBlockchain2
from time import time

if __name__ == "__main__":
    messaging_blockchain = PyBasicBlockchain2.MessagingBlockchain()  # Create a new blockchain 🆕

    # Customize the blockchain
    messaging_blockchain.difficulty = 5  # Increase difficulty
    messaging_blockchain.mining_reward = 2  # Increase mining reward

    # Add some messages 📩
    messaging_blockchain.add_message({"sender": "Alice", "recipient": "Bob", "content": "Hello, Bob!", "timestamp": time()})
    messaging_blockchain.add_message({"sender": "Bob", "recipient": "Alice", "content": "Hi, Alice!", "timestamp": time()})

    print("Mining pending messages...⛏️")
    messaging_blockchain.mine_pending_messages("Miner1")  # Mine those messages! 🤑

    # Add more messages 📩
    messaging_blockchain.add_message({"sender": "Charlie", "recipient": "Dave", "content": "Hey Dave, long time no see!", "timestamp": time()})
    messaging_blockchain.add_message({"sender": "Dave", "recipient": "Charlie", "content": "Hey Charlie, indeed! How have you been?", "timestamp": time()})

    print("Mining pending messages...⛏️")
    messaging_blockchain.mine_pending_messages("Miner2")  # Another round of mining! 💰

    # Print the details of each block in the chain 🧱
    for block in messaging_blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash} - Previous Hash: {block.previous_hash}")
        print("Messages:", block.messages)
        print("Nonce:", block.nonce)
        print()

    # Check if the blockchain is still valid ✅
    print("Is blockchain valid?", messaging_blockchain.is_chain_valid())

    # Get messages for a specific user 🕵️‍♂️
    print("Messages for Bob:", messaging_blockchain.get_user_messages("Bob"))
    print("Messages for Alice:", messaging_blockchain.get_user_messages("Alice"))
    print("Messages for Dave:", messaging_blockchain.get_user_messages("Dave"))

    # Get the entire message history for a user 🕵️‍♀️
    print("Message history for Charlie:", messaging_blockchain.get_user_history("Charlie"))
    
    # Get the total message count 🧾
    print("Total number of messages in blockchain:", messaging_blockchain.get_message_count())
```

## Known Bugs 🐞
- The current implementation has a known issue where the blockchain validation fails due to hash mismatches. For example:
```shell
Block 1 hash mismatch: 000056ccfdd3c323f561a7a5aa736b918ec8300190c7ad76f71a7cdff0af5a5a != 5c82a22c32bd3232f1d8fcb129198a3ab521041cbe52001a7339d0fa1cc1df1e
Is blockchain valid? False
```

- This bug affects the is_chain_valid method, and fixing it will involve troubleshooting the hash computation and block validation logic.

*FOR MORE INFO SEE `./KRAZY.md`*
