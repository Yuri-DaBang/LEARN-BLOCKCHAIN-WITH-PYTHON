import hashlib
import json
from time import time
from typing import List, Dict, Any

class MessageBlock:
    def __init__(self, index: int, timestamp: float, messages: List[Dict[str, Any]], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.messages = messages
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()  # Compute the initial hash

    def compute_hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        required_prefix = '0' * difficulty
        while not self.hash.startswith(required_prefix):
            self.nonce += 1
            self.hash = self.compute_hash()

class MessagingBlockchain:
    def __init__(self):
        self.chain: List[MessageBlock] = []
        self.pending_messages: List[Dict[str, Any]] = []
        self.difficulty = 4
        self.mining_reward = 1
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = MessageBlock(0, time(), [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_last_block(self) -> MessageBlock:
        return self.chain[-1]

    def add_message(self, message: Dict[str, Any]):
        self.pending_messages.append(message)

    def mine_pending_messages(self, miner_address: str):
        self.pending_messages.append({
            "sender": "Network",
            "recipient": miner_address,
            "content": f"Mining reward: {self.mining_reward}",
            "timestamp": time()
        })
        new_block = MessageBlock(
            index=len(self.chain),
            timestamp=time(),
            messages=self.pending_messages.copy(),
            previous_hash=self.get_last_block().hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_messages = []

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                print(f"Block {current_block.index} hash mismatch: {current_block.hash} != {current_block.compute_hash()}")
                return False
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} previous hash mismatch: {current_block.previous_hash} != {previous_block.hash}")
                return False
        return True

    def get_user_messages(self, user_address: str) -> List[Dict[str, Any]]:
        user_messages = []
        for block in self.chain:
            for message in block.messages:
                if message['recipient'] == user_address:
                    user_messages.append(message)
        return user_messages

    def get_sent_messages(self, user_address: str) -> List[Dict[str, Any]]:
        sent_messages = []
        for block in self.chain:
            for message in block.messages:
                if message['sender'] == user_address:
                    sent_messages.append(message)
        return sent_messages

    def get_user_history(self, user_address: str) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "received": self.get_user_messages(user_address),
            "sent": self.get_sent_messages(user_address)
        }
