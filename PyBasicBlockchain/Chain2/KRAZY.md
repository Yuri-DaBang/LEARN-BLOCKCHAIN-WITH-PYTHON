# MessagingBlockchain 📡🚀

*LET'S GET CRAZY WITH BLOCKCHAIN MESSAGING!*

- Welcome to the wild world of testing with the MessagingBlockchain class! Buckle up as we push this messaging blockchain to its limits and see how it handles a variety of scenarios. Let’s dive in!

## Setup 🛠️
- Ensure you have the MessagingBlockchain class ready to go. Here’s a quick setup:
- 
```python
from messaging_blockchain import MessagingBlockchain  # Import our MessagingBlockchain library!
```

## Test 1: Massive Message Flood 🚿
### Test Code
```python
blockchain = MessagingBlockchain()  # Start a new messaging blockchain. 🆕

# Add a massive flood of messages.
for i in range(1000):
    blockchain.add_message({"sender": f"Alice_{i}", "recipient": f"Bob_{i}", "content": f"Message {i}", "timestamp": time()})

print("Mining pending messages...")
blockchain.mine_pending_messages("FloodMiner")  # Mine those messages into a new block. ⛏️

# Print the details of the mined block.
last_block = blockchain.get_last_block()
print(f"Block {last_block.index} - Hash: {last_block.hash} - Previous Hash: {last_block.previous_hash}")
print("Messages count:", len(last_block.messages))  # How many messages did we pack in?
print("Nonce:", last_block.nonce)
```
### Case Study
*Why This Test?*
- This test evaluates the blockchain's ability to handle a large number of messages. By adding 1,000 messages and mining them, we can observe how well the system processes and packs these messages into a single block, testing scalability and efficiency.


## Test 2: Extreme Mining Difficulty 🏋️‍♂️
### Test Code
```python
blockchain.difficulty = 6  # Increase mining difficulty. 🎯

blockchain.add_message({"sender": "ExtremeAlice", "recipient": "ExtremeBob", "content": "High difficulty test", "timestamp": time()})
blockchain.add_message({"sender": "ExtremeBob", "recipient": "ExtremeCharlie", "content": "Difficulty challenge", "timestamp": time()})

print("Mining pending messages...")
blockchain.mine_pending_messages("ExtremeMiner")  # This will take a while! ⛏️

# Print the details of the mined block.
last_block = blockchain.get_last_block()
print(f"Block {last_block.index} - Hash: {last_block.hash} - Previous Hash: {last_block.previous_hash}")
print("Messages count:", len(last_block.messages))
print("Nonce:", last_block.nonce)
```
### Case Study
*Why This Test?*
- By increasing the mining difficulty, we test how well the blockchain handles challenging mining conditions. This helps us understand the impact of difficulty on mining time and overall blockchain security.

## Test 5: User Message History 📜
### Test Code
```python
blockchain.add_message({"sender": "Alice", "recipient": "Bob", "content": "Message for Bob", "timestamp": time()})
blockchain.add_message({"sender": "Bob", "recipient": "Alice", "content": "Reply from Bob", "timestamp": time()})

print("Mining pending messages...")
blockchain.mine_pending_messages("HistoryMiner")

# Get message history for users.
print("Message history for Bob:", blockchain.get_user_history("Bob"))
print("Message history for Alice:", blockchain.get_user_history("Alice"))
```
### Case Study
*Why This Test?*
- This test ensures the functionality of retrieving user message histories. By querying the message history for different users after several transactions, we confirm that the system accurately tracks and returns past messages.


## Known Bugs 🐞
- The current implementation has a known issue where the blockchain validation fails due to hash mismatches. For example:
```shell
Block 1 hash mismatch: 000056ccfdd3c323f561a7a5aa736b918ec8300190c7ad76f71a7cdff0af5a5a != 5c82a22c32bd3232f1d8fcb129198a3ab521041cbe52001a7339d0fa1cc1df1e
Is blockchain valid? False
```

- This bug affects the is_chain_valid method, and fixing it will involve troubleshooting the hash computation and block validation logic.


## Chat App Example 💬
*About the App*
- Real-Time Messaging App with MessagingBlockchain
- It uses socket connections to chat and PyBasicBlockchain2 to save the messages in a blockchain format in a .json file
*The application will include:*
  - A console interface for sending and receiving messages.
  - Real-time updates to show incoming messages.
*How to get the app*
- Navigate to `/Chain2/ChatApp` and there you go!
  - Two code files namely `ChatApp.py` and `ChatServer.py` will be there and the good old `PyBasicBlockchain2.py`
  - `ChatApp.py` is basically the chat client (User Interface).
  - `ChatServer.py` is the server.
*More on App*
  - Read the `/Chain2/ChatApp/CHATAPP.md` for more info!

## Conclusion 🎉
- These tests and the example chat app give you a solid starting point to explore the capabilities of the MessagingBlockchain class. Feel free to tweak the tests and app to better suit your needs. Happy testing and coding! 🚀💬
