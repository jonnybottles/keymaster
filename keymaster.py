import os
import paramiko
from getpass import getpass

# Function to get server details from the user
def get_server_details():
  """
  Prompts the user for the IP address, username, and password
  of the SSH server and returns them as a tuple.
  """
  ip_address = input("Enter the IP address of the SSH server: ")
  username = input("Enter the username for the SSH server: ")
  password = getpass("Enter the password for the SSH server: ")
  return ip_address, username, password

# Function to generate SSH key pair if it doesn't exist
def generate_ssh_keys():
  """
  Checks if an SSH key pair (id_rsa and id_rsa.pub) exists in the
  user's ~/.ssh directory. If not found, it creates a new RSA key pair
  using the `ssh-keygen` command.
  """
  ssh_dir = os.path.expanduser('~/.ssh')
  os.makedirs(ssh_dir, exist_ok=True)  # Create the directory if it doesn't exist
  private_key_path = os.path.join(ssh_dir, 'id_rsa')
  os.system(f'ssh-keygen -t rsa -N "" -f {private_key_path}')  # Generate keys silently

# Function to send the public key to the remote server
def send_public_key(ip_address, username, password):
  """
  Attempts to connect to the SSH server using the provided credentials.
  If successful, it reads the public key content from the local file
  and sends it to the server, appending it to the authorized_keys file
  on the remote server user's ~/.ssh directory.
  """
  try:
    print("Connecting to the server...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept host key
    ssh.connect(ip_address, username=username, password=password)

    print("Sending public key to the server...")
    public_key_path = os.path.join(os.path.expanduser('~/.ssh'), 'id_rsa.pub')
    with open(public_key_path, 'r') as f:
      public_key = f.read()
    ssh.exec_command(f'echo "{public_key}" >> ~/.ssh/authorized_keys')
    print("Public key sent successfully.")

  except Exception as e:
    print("Failed to send public key:", e)
  finally:
    ssh.close()  # Close the SSH connection (optional but good practice)

# Main execution function
def main():
  """
  Calls the `get_server_details` function to get server information
  and then checks for existing SSH keys. If keys are missing, it generates
  a new pair using `generate_ssh_keys`. Finally, it attempts to send
  the public key to the server using `send_public_key`.
  """
  ip_address, username, password = get_server_details()

  if not os.path.exists(os.path.join(os.path.expanduser('~/.ssh'), 'id_rsa')):
    generate_ssh_keys()

  send_public_key(ip_address, username, password)

# Entry point for the script execution
if __name__ == "__main__":
  main()
