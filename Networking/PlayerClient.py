import socket, pickle


class PlayerClient():
    host = str
    port = int

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def sentPacket(self, packet: str):
        clientSocketFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocketFile.connect((self.host, self.port))

        clientSocketFile.sendall(bytes(packet.encode('utf-8')))

        print(clientSocketFile.recv(50))

        clientSocketFile.close()

    # ip = str(input("Ip Address: "))
