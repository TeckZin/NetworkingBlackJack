import socket

sockFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234

# binding any network interface to the port number
sockFile.bind(('', port))

while True:
    # the que to connect to the server
    sockFile.listen(30)

    # addr = ip, cs is the data == client socket
    cs, addr = sockFile.accept()

    print(addr)

    message = cs.recv(1024)
    print(message)

    cs.send(bytes('Accept', 'utf-8'))

cs.close()
s.close()