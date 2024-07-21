import socket  # We need sockets for chatting, like the post office of the internet!
import json    # JSON is our way of sending messages in a format that everyone understands.
import os      # For checking if files exist and making directories. Like a digital handyman!
import random  # To generate random file names. Who doesn't like randomness?
import string  # For creating those random names with letters and numbers. No emojis here, sadly!
from threading import Thread  # To let multiple people chat at the same time. It's like multitasking for our chat server!
from time import time  # To add timestamps to our messages, so we know who was late to the party.

# Server configuration
SERVER_HOST = 'localhost'  # Where our server lives. It's on your computer, not in the cloud!
SERVER_PORT = 5000         # The door number to our server. Knock here to chat!
BLOCKCHAIN_DIR = 'Blockchain_Tables'  # Directory where we keep our chat history. Like a digital attic.
CHAT_FILE = os.path.join(BLOCKCHAIN_DIR, 'Chatblockchain.json')  # File where we'll save the chat. It's like a diary, but less embarrassing.

# Ensure the Blockchain_Tables directory exists
os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)  # Create the directory if it doesn't exist. Because who likes errors?

# Generate a random filename
def generate_random_filename(length=20):
    # Make a random file name to avoid overwriting the existing one. It's like hiding your treasure in a secret location!
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + '.json'

# Create a new file if Chatblockchain.json exists
if os.path.exists(CHAT_FILE):
    # If the file already exists, make a new file with a random name. No one wants a file collision!
    CHAT_FILE = os.path.join(BLOCKCHAIN_DIR, generate_random_filename())

def save_message_to_file(message):
    # Save the message to the file. Think of it as scribbling on a notepad.
    with open(CHAT_FILE, 'a') as file:
        file.write(json.dumps(message) + '\n')  # Write the message to the file in JSON format.

def handle_client(client_socket, address):
    # Handle incoming chat from each client. It's like being the host of a digital party.
    print(f"Connection from {address}")  # Announce who’s joining the party!

    username = client_socket.recv(1024).decode('utf-8')  # Get the username. It’s like checking the guest list.
    welcome_message = f"{username} has joined the chat."  # Create a welcome message. Everyone loves a warm welcome!
    broadcast(welcome_message, client_socket)  # Announce the new guest to everyone else.

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')  # Receive a message from the client. Like opening a letter.
            if message:
                if message.lower() == 'exit':
                    # Handle the case where someone wants to leave the party. We need to say goodbye!
                    goodbye_message = f"{username} has left the chat."
                    broadcast(goodbye_message, client_socket)
                    break

                message_to_save = {
                    'username': username,
                    'message': message,
                    'timestamp': time()  # Add a timestamp to the message. Because time flies when you're having fun!
                }
                save_message_to_file(message_to_save)  # Save the message to our digital diary.

                broadcast(f"{username}: {message}", client_socket)  # Broadcast the message to everyone else.
            else:
                break  # If no message, break out of the loop. The client is probably done chatting.
        except:
            break  # Handle exceptions. Because sometimes, things go wrong and we need to break out.

    client_socket.close()  # Close the connection. The party's over for this guest.

def broadcast(message, client_socket):
    # Send the message to all clients except the sender. It’s like announcing news to everyone at the party.
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))  # Send the message to the client. Time to spread the gossip!
            except:
                client.close()  # Close the connection if sending fails. Nobody likes a broken chat!
                clients.remove(client)  # Remove the client from the list of active clients.

def start_server():
    # Start the server. It’s like opening the doors to the chat party.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket. This is the digital doorbell.
    server.bind((SERVER_HOST, SERVER_PORT))  # Bind the socket to the host and port. Like assigning a specific address.
    server.listen(5)  # Listen for incoming connections. We’re ready for guests!
    print("Server listening...")  # Let everyone know the server is ready and waiting.

    while True:
        client_socket, client_address = server.accept()  # Accept a new client. Welcome them to the party!
        clients.append(client_socket)  # Add the new client to the list of active clients.
        client_handler = Thread(target=handle_client, args=(client_socket, client_address))  # Handle each client in a new thread.
        client_handler.start()  # Start the thread. Time for some multitasking!

clients = []  # List of active clients. Our guest list!

if __name__ == "__main__":
    start_server()  # Start the server if this file is run directly. Time to kick off the party!
