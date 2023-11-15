import socket


def sendPacket(message: str, host, port):
    clientSocketFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocketFile.connect((host, port))

    clientSocketFile.sendall(bytes(message.encode('utf-8')))

    print(clientSocketFile.recv(50))

    clientSocketFile.close()

    # ip = str(input("Ip Address: "))
