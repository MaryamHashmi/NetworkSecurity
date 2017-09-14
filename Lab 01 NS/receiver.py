#receiver

import socket
import sys

import decrypt

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print "Receiver waiting for message.\n\n"
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)


connection, client_address = sock.accept()
while True:
    message = connection.recv(1024)
    if len(message)> 0:
        print "Message: " + decrypt.decrypt(message)
connection.close()