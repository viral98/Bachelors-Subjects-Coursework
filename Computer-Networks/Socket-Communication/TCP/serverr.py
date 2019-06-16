import socket
import threading

bind_ip = '127.0.0.1'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print 'Listening on {}:{}'.format(bind_ip, bind_port)


while True:
    client_socket, address = server.accept()
    print 'Accepted connection from {}:{}'.format(address[0], address[1])
    request = client_socket.recv(1024)
    print 'Received {}'.format(request)
    client_socket.send('ACK!')
    client_socket.close()