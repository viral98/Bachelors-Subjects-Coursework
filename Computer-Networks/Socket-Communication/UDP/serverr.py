import socket
import threading

bind_ip = '127.0.0.1'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip, bind_port))

print 'Listening on {}:{}'.format(bind_ip, bind_port)


while True:
    data, addr = server.recvfrom(1024)
    print "Message: ", data
    server.sendto('HELLO FROM SERVER',(addr))