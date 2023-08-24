import paramiko
import time

# Update the following lines with your server's information
host = "tty.sdf.org"
username = "jcal0"
password = "ZVTKoZ9HfPRQ"

# Connect to the remote server
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

# Open an interactive shell session
shell = client.invoke_shell()

# Wait for the shell to initialize
time.sleep(1)

# Send the backspace key (ASCII code 8) twice to simulate pressing the backspace key
shell.send("\x08")
shell.send("\x08")

# Wait for the command to execute and output to accumulate
time.sleep(1)

# Receive and print the output
output = shell.recv(4096).decode()
print(output)

# Close the shell and the SSH connection
shell.close()
client.close()
