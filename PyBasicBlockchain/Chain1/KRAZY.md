# Crazy Tests with PyBasicBlockchain Lib V1 🧪😜
*LETS GET STARTED*

- Welcome to the crazy testing ground for PyBasicBlockchain Lib V1! Here, we will push the limits of our blockchain library and see how it handles various wild scenarios. Get ready for some fun and unexpected results!

## Setup 🛠️

First, make sure you have the library installed and ready to go:

```python
import PyBasicBlockchain  # Import the awesome PyBasicBlockchain library! 🚀
```

## Test 1: Mega Transaction Flood 🚿
- Let's see how the blockchain handles a massive flood of transactions.
### Test Code
```python
blockchain = PyBasicBlockchain.Blockchain()  # Start a new blockchain. 🆕

# Add a huge number of transactions.
for i in range(1000):
    blockchain.add_transaction({"sender": f"Alice_{i}", "recipient": f"Bob_{i}", "amount": i})

print("Mining pending transactions...")
blockchain.mine_pending_transactions("MegaMiner")  # Mine those transactions into a new block. ⛏️

# Print the details of the mined block.
last_block = blockchain.get_last_block()
print(f"Block {last_block.index} - Hash: {last_block.hash} - Previous Hash: {last_block.previous_hash}")
print("Transactions count:", len(last_block.transactions))  # How many transactions did we manage to pack in?
print("Nonce:", last_block.nonce)
```
### Case Study
*Why This Test?*
- This test is designed to evaluate how well the blockchain handles a large number of transactions. By flooding the blockchain with 1,000 transactions, we can observe the system's performance and see if it effectively processes and mines all these transactions in a single block. It’s a way to test the scalability and efficiency of our mining process.

## Test 2: Insane Difficulty Challenge 🏋️‍♂️

### Test Code

```python
blockchain.difficulty = 6  # Increase the difficulty. 🎯

blockchain.add_transaction({"sender": "InsaneAlice", "recipient": "InsaneBob", "amount": 100})
blockchain.add_transaction({"sender": "InsaneBob", "recipient": "InsaneCharlie", "amount": 50})

print("Mining pending transactions...")
blockchain.mine_pending_transactions("InsaneMiner")  # This might take a while... ⛏️

# Print the details of the mined block.
last_block = blockchain.get_last_block()
print(f"Block {last_block.index} - Hash: {last_block.hash} - Previous Hash: {last_block.previous_hash}")
print("Transactions count:", len(last_block.transactions))
print("Nonce:", last_block.nonce)
```

### Case Study
*Why This Test?*
- This test increases the mining difficulty to see how the blockchain performs under more challenging conditions. By setting a high difficulty level, we simulate a scenario where mining takes significantly longer. This helps us understand how changes in difficulty impact mining time and blockchain security.

## Test 3: Rapid Fire Mining 🔫

### Test Code

```python
blockchain.difficulty = 2  # Lower the difficulty for rapid mining. 🎯

# Add some transactions and mine blocks rapidly.
for i in range(10):
    blockchain.add_transaction({"sender": f"RapidAlice_{i}", "recipient": f"RapidBob_{i}", "amount": i * 10})
    blockchain.mine_pending_transactions(f"RapidMiner_{i}")
    last_block = blockchain.get_last_block()
    print(f"Block {last_block.index} mined - Hash: {last_block.hash}")
```

### Case Study
*Why This Test?*
- This test examines the blockchain's ability to handle rapid mining operations. By lowering the difficulty and mining multiple blocks in quick succession, we can assess how well the system maintains performance and integrity when processing transactions and creating new blocks at a fast pace.

## Test 4: Chain Tampering Attempt 🚨

### Test Code

```python
blockchain.add_transaction({"sender": "TamperAlice", "recipient": "TamperBob", "amount": 999})
blockchain.mine_pending_transactions("TamperMiner")

# Tamper with the blockchain by changing a transaction.
print("Attempting to tamper with the blockchain...")
blockchain.chain[1].transactions[0]['amount'] = 1000000  # Sneaky tampering! 🕵️‍♂️

# Check if the blockchain is still valid.
print("Is blockchain valid after tampering?", blockchain.is_chain_valid())  # Expecting a big fat NO. ❌
```

### Case Study
*Why This Test?*
- This test is designed to simulate a chain tampering scenario. By altering a transaction in an already mined block, we check if the blockchain can detect this manipulation. This helps us validate the robustness and security of the blockchain's integrity checks.

## Test 5: Balance Check Shenanigans 💰

### Test Code

```python
# Check balances of various users.
print("Balance of MegaMiner:", blockchain.get_balance("MegaMiner"))
print("Balance of InsaneMiner:", blockchain.get_balance("InsaneMiner"))
print("Balance of RapidMiner_0:", blockchain.get_balance("RapidMiner_0"))
print("Balance of RapidMiner_9:", blockchain.get_balance("RapidMiner_9"))
print("Balance of TamperAlice:", blockchain.get_balance("TamperAlice"))
print("Balance of TamperBob:", blockchain.get_balance("TamperBob"))
```

### Case Study
*Why This Test?*
- This test checks the balance calculation for different users. By querying the balance of various addresses after several transactions and mining operations, we ensure that the balance calculations are accurate and reflect the state of the blockchain. This helps verify that transaction processing and reward distribution are functioning correctly.


# Conclusion 🎉
- These tests are just the beginning. Feel free to experiment further and create your own tests to explore the capabilities and limits of the PyBasicBlockchain library. Have fun and happy testing! 🚀💡
