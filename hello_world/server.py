import socket

comms_socket = socket.socket()
comms_socket.bind(('localhost',50000))
comms_socket.listen(10)
connection,address =  comms_socket.accept()

while True:
    print(connection.recv(4096).decode("UTF-8"))
    send_data = input("Reply:")
    connection.send(bytes(send_data,"UTF-8"))