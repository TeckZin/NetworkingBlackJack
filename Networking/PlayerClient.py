import socket, pickle
from BlackJackGame import PacketPlayer

class PlayerClient:
    def __init__(self):
        ip = str(input("Ip Address: "))
        port = 1234

        answer = str(input("Connect: "))
        if answer.upper() == "Y":
            packet = PacketPlayer.PacketPlayer(True)
            self.sentPacket(ip, port, packet)


    def sentPacket(self, host, port, packet):
        clientSocketFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocketFile.connect((host, port))

        dataString = pickle.dumps(packet)
        clientSocketFile.send(dataString)

        print(clientSocketFile.recv(50))

        clientSocketFile.close()








