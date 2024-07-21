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
