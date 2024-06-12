# Key Master

Key Master is a simple Python script automates the process of generating an SSH key pair (if it doesn't already exist) and securely adding the public key to a remote server for passwordless login

## Requirements:

Python 3 (https://www.python.org/downloads/)
paramiko library (pip install paramiko)

## Installation:

Save the script as ssh_key_manager.py.

Install paramiko: pip install paramiko

## Usage:

Run the script: python ssh_key_manager.py
Follow the prompts to enter:
The server's IP address
Username for the SSH server
Password for the SSH server (Security Note: consider passwordless SSH login for better security)


## Functionality:

**Retrieves Server Details:** Prompts for the server's IP address, username, and password.

**Generates SSH Keys (if necessary):** Checks for an existing SSH key pair (id_rsa and id_rsa.pub) in your ~/.ssh directory. If not found, generates a new RSA key pair using ssh-keygen.

**Connects to Server:** Establishes an SSH connection using paramiko. Automatically accepts the server's host key (Security Note: consider verifying the fingerprint manually for production environments).

**Sends Public Key:** Reads the public key content and sends it to the server, appending it to the authorized_keys file on the remote server user's ~/.ssh directory.

**Provides Feedback:** Displays success or failure messages based on the connection and key transfer.

## Disclaimer

This script assumes the server allows SSH connections on the default port (22).
The script uses paramiko.AutoAddPolicy() for automatic host key acceptance. For production environments, manually verify the host key fingerprint before adding it.
Disclaimer:

Use this script at your own risk. The author is not responsible for any damage or misuse.
