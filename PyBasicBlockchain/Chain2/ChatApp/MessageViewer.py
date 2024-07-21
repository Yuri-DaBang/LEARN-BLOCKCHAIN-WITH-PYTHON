import json
import os
import random
import sys
import argparse
import time
from termcolor import colored

# Colors for terminal output
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

def load_messages(file_path):
    """Load messages from the specified JSON file."""
    if not os.path.isfile(file_path):
        # Check if the file exists at the given path
        print(f"File not found: {file_path}")
        sys.exit()  # Exit the program if the file is not found

    messages = []  # List to hold all messages
    with open(file_path, 'r') as file:
        # Open the file in read mode
        for line in file:
            try:
                # Attempt to parse each line of the file as JSON
                messages.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                # Print an error message if JSON decoding fails
                print(f"Error decoding JSON: {line.strip()}")
    return messages

def assign_colors(users):
    """Assign a unique color to each user."""
    user_colors = {}  # Dictionary to hold user-color pairs
    available_colors = COLORS.copy()  # Copy of the COLORS list to shuffle and use
    random.shuffle(available_colors)  # Shuffle colors to ensure randomness

    for user in set(users):
        # Iterate over unique users
        if available_colors:
            # Assign a unique color if available
            user_colors[user] = available_colors.pop()
        else:
            # Reuse colors if we run out
            user_colors[user] = random.choice(COLORS)

    return user_colors

def display_messages(messages, user_colors):
    """Display messages with unique colors for each user."""
    for msg in messages:
        username = msg['username']  # Extract the username from the message
        message = msg['message']    # Extract the message text
        timestamp = msg['timestamp']  # Extract the timestamp

        color = user_colors.get(username, 'white')  # Get the color for the user, default to 'white'
        formatted_message = f"[{timestamp:<18}] {username:<13} : {message}"  # Format the message for display
        time.sleep(0.2)  # Pause for a short duration to simulate real-time message flow
        print(colored(formatted_message, color))  # Print the message with the assigned color

def main():
    parser = argparse.ArgumentParser(description='Display messages from a JSON file.')
    # Create an argument parser for command-line arguments
    parser.add_argument('file', type=str, help='Path to the JSON file containing chat messages')
    # Add an argument for the file path
    args = parser.parse_args()  # Parse the command-line arguments

    file_path = args.file  # Get the file path from the arguments

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Message file does not exist: {file_path}")
        return  # Exit if the file does not exist

    messages = load_messages(file_path)  # Load messages from the file

    if not messages:
        print("No messages to display.")
        return  # Exit if there are no messages

    users = [msg['username'] for msg in messages]  # Extract usernames from messages
    user_colors = assign_colors(users)  # Assign colors to users

    display_messages(messages, user_colors)  # Display the messages with colors

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
