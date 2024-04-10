# Reverse Shell Application

To run the code, first start the server by running the command python `server.py` then start the client by running `python client.py`. The client will connect to the server and the server will be able to send commands to the client. The client will execute the commands and send the output back to the server.

This application allows for remote access to a target machine (client) from an attacker's machine (server) over a TCP connection. The server and client use the same IP address and port number to establish a connection. Configuration settings, such as `server_ip` and `server_port`, can be modified in the `settings.json` file.

## Setting Up the Application

1. Modify the `settings.json` file to specify the `server_ip` and `server_port` for the connection.
2. Choose a common port for the reverse shell, such as 80, 443, 8080, 139, or 445, to ensure traffic is allowed.

## Known Issues

- Commands that don't return any output can cause the program to freeze. Implement a mechanism in the client to handle such scenarios.

## Custom Commands

- There is a custom command `search_password <path to directory>` that prompts the client to execute a bash script that searches for a password file in the given directory. This script uses the `find` command to recursively look for a specified file that has the text “password” in the name and returns a list of file paths to the server for files found under that criteria.
