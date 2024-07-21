import socket  # We need sockets for chatting, like the internet's version of a telephone line.
from threading import Thread  # To handle incoming messages while letting you type. It's multitasking at its finest!
import sys  # For exiting the program. Because sometimes, we need to hit the eject button!

# Client configuration
SERVER_HOST = 'localhost'  # The server’s address. In this case, it’s running on your own computer.
SERVER_PORT = 5000         # The port number. Think of it as the server’s specific phone line.

def receive_messages(client_socket):
    # This function will keep checking for new messages from the server.
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')  # Receive a message. It's like catching a letter from the post office.
            if message:
                print(message)  # Display the message. The chat window is where it all happens!
            else:
                break  # If there's no message, it means the server might be gone. Time to break out of the loop.
        except:
            print("Connection lost.")  # If something goes wrong, let the user know the connection has been lost.
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket. This is our connection to the server.
    client_socket.connect((SERVER_HOST, SERVER_PORT))  # Connect to the server. It's like dialing in to the chat party!

    username = input("Enter your username: ")  # Ask for the user's name. We need to know who’s chatting.
    client_socket.send(username.encode('utf-8'))  # Send the username to the server. Time to introduce yourself!

    receive_thread = Thread(target=receive_messages, args=(client_socket,))  # Start a new thread to receive messages. Like having a personal assistant!
    receive_thread.start()

    while True:
        message = input()  # Get a message from the user. What’s on your mind?
        if message.lower() == 'exit':
            client_socket.send(message.encode('utf-8'))  # Send an exit message to the server. Time to say goodbye!
            break
        client_socket.send(message.encode('utf-8'))  # Send the message to the server. Share your thoughts with everyone!

    client_socket.close()  # Close the connection when done. No more chat, no more connection.
    sys.exit()  # Exit the program. It’s like finally hitting the end of the chat session!

if __name__ == "__main__":
    main()  # Run the main function. Let the chatting begin!
