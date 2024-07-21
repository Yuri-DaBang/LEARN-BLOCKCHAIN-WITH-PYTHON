# Real-Time Chat Application

Welcome to the Real-Time Chat Application! This application consists of a chat server and client built using Python's socket and threading libraries. It supports real-time messaging and saves chat logs to a file. Below you'll find detailed instructions on how to set up and run the server and client applications.

## Overview

The chat application includes two main components:

1. **Chat Server** - Manages incoming client connections, broadcasts messages to all connected clients, and saves messages to a file.
2. **Chat Client** - Connects to the server, allows users to send messages, and displays received messages in real-time.

## Files

### `ChatServer.py`

This is the chat server script. It listens for incoming client connections, handles messages, and saves chat logs.

#### Key Features
- **Client Handling:** Manages multiple clients simultaneously using threading.
- **Message Broadcasting:** Sends received messages to all connected clients.
- **Message Logging:** Saves messages to a JSON file.

#### Usage
1. Ensure you have Python installed.
2. Run the server using:
   ```bash
   python ChatServer.py
   ```
3. The server will listen for incoming connections on localhost and port 5000.

### `ChatApp.py`

This is the chat client script. It connects to the server, sends messages, and displays received messages.

#### Key Features
- **User Authentication:** Prompts the user to enter a username.
- **Message Sending:** Allows users to send messages to the chatroom.
- **Real-Time Messaging:** Receives and displays messages from the server in real-time.

#### Usage
1. Ensure you have Python installed.
2. Run the client using:
   ```bash
   python ChatApp.py
   ```
3. Enter your username when prompted and start sending messages.

### `MESSAGE_VIEWER.PY`

This is a chat message viewer script. It reads chat messages from a JSON file and displays them in the terminal with unique colors for each user.

#### Key Features
- **Dynamic User Colors:** Each user gets a unique color every time the script runs.
- **JSON File Reading:** Loads and parses messages from a specified JSON file.
- **Colorful Terminal Output:** Displays messages with different colors for each username, making it easier to distinguish between different users.

#### Usage
1. **Install Python and Dependencies:**
    - Ensure you have Python 3 installed.
    - Install the `termcolor` library using pip:
      ```bash
      pip install termcolor
      ```

2. **Prepare the Message File:**
    - Place your chat messages in a JSON file.
    - The file should be located at `./Blockchain_Tables/Chatblockchain.json` or modify the `FILE_PATH` variable in the script to point to your file.

3. **Run the Script:**
    - Execute the script using:
      ```bash
      python MESSAGE_VIEWER.PY
      ```

4. **View Output:**
    - The script will display messages with each user's text in a different color.
    - Each time you run the script, users will be assigned different colors.

#### Example Output
When you run the script, you will see messages displayed in different colors:
*Example1*
```bash
>> python MessageViewer.py Blockchain_Tables/Chatblockchain.json
[1721559122.4003148] Donald Trump  : Bro I Got sHOT
[1721559170.919527 ] Joe Biden     : You got what, `sHOT` what is this
[1721559180.4346414] Donald Trump  : I got shot on the ea
[1721559196.038511 ] Joe Biden     : what are you trying to say , what is `ea`
[1721559203.4399083] Joe Biden     : did you mean ear
[1721559207.900358 ] Donald Trump  : yeeeaahhh
[1721559215.7501202] Joe Biden     : why didnt you die
[1721559248.1639333] North Korea Secret Service : dont be racist biden
[1721559260.785625 ] North Korea Secret Service : but that wasnt me
[1721559279.744182 ] Joe Biden     : sorry trump
[1721559286.2104378] Joe Biden     : but i am happy you alive
[1721559294.0992258] Donald Trump  : thanks biden
[1721559305.6627536] Donald Trump  : and BTW, i am winning election this year
[1721559315.4680612] Joe Biden     : noooooooooooo!!!!
[1721559334.400022 ] North Korea Secret Service : but but but, i am the king
```

*Example2*
```bash
>> python MessageViewer.py Blockchain_Tables/HpDsk6cw25sFxv2sW0pn.json
Current working directory: E:\fri3nds\y-category-Projects\Thorium Org\blockchain\pybasicblockchain\chain2\chatapp
Checking file path: Blockchain_Tables/HpDsk6cw25sFxv2sW0pn.json
[1721560871.015322 ] MrBeast       : hey gang
[1721560874.180472 ] MrBeast       : i am mrbeast
[1721560876.7476213] MrBeast       : i am rich
[1721560883.4956124] MrBeast       : i am powerfull
[1721560887.2829814] MrBeast       : i am handsome
[1721560913.8607244] KSI           : About that, you are ugly beastboy
[1721560920.2684956] KSI           : UGLY AS HELL
[1721560926.451915 ] MrBeast       : hey
[1721560954.8572006] iShowSpeed    : hey, dont be rude @KSI
[1721560972.3164132] KSI           : whats up with you, DAWG
[1721560976.5645943] KSI           : Black Dawg
[1721560991.1239848] iShowSpeed    : Bark Bark Bark Bark Bark
[1721560992.3981922] iShowSpeed    : Bark Bark
[1721560994.777618 ] iShowSpeed    : Bark Bark Bark Bark
[1721561018.2614205] KSI           : yo dawg , you are actually not a DAWG , sorry but you are a dog
[1721561029.7264338] MrBeast       : ha ha ha
[1721561030.7904382] MrBeast       : LOL
[1721561032.6990037] MrBeast       : LMAO
[1721561044.9255238] iShowSpeed    : YO MRBEAST
[1721561048.3313198] iShowSpeed    : what the hell
```

- Usernames will be in various colors, making the chat history visually distinct and engaging.

#### Troubleshooting
- **File Not Found:** Ensure the JSON file exists at the specified path. Update the `FILE_PATH` variable if needed.
- **Empty File:** The script will inform you if the file is empty or cannot be read.

## File Structure

The chat server saves messages to a file in the ./Blockchain_Tables directory. If Chatblockchain.json already exists, a new file with a random 20-digit name is created.

#### Troubleshooting
- **ModuleNotFoundError:** Ensure that you are running the scripts from the correct directory and that all necessary modules are installed.
- **Connection Issues:** Verify that the server is running before starting the client. Ensure that the server address and port are correctly configured.

# License
This project is licensed under the MIT License. See the `./LICENSE.md` file for details.




