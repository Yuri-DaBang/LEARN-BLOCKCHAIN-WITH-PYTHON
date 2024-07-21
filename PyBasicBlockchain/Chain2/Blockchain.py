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
