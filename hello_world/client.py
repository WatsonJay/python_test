import socket

comms_socket = socket.socket()
comms_socket.connect(('localhost',50000))
while True:
    send_data = input("message:")
    comms_socket.send(bytes(send_data,"UTF-8"))
    print(comms_socket.recv(4096).decode("UTF-8"))