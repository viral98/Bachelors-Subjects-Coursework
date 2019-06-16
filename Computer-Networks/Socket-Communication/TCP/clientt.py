import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9999))

client.send('HELLO FROM CLIENT')

response = client.recv(4096)

print response