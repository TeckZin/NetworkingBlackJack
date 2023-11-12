import socket, pickle
from BlackJackGame import PacketPlayer


class PlayerClient():
    host = str
    port = int

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def sentPacket(self, packet: PacketPlayer):
        clientSocketFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocketFile.connect((self.host, self.port))

        dataString = pickle.dumps(packet)
        clientSocketFile.send(dataString)

        print(clientSocketFile.recv(50))

        clientSocketFile.close()


    # ip = str(input("Ip Address: "))

