import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto('HELLO FROM CLIENT',('127.0.0.1',9999))

response, addr = client.recvfrom(1024)

print response