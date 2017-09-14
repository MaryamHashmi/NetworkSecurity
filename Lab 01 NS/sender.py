# Sender

import socket
import sys

import encrypt

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print "Connecting...\n\n"
sock.connect(server_address)

while True:
    # Send data
    message = raw_input('Enter a message: ')
    encrypted_message = encrypt.encrypt(message)
    sock.sendall(encrypted_message)




