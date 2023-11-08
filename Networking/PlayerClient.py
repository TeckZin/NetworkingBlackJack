import socket, pickle
from BlackJackGame import PacketPlayer


def sentPacket(self, host, port, packet):
    clientSocketFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocketFile.connect((host, port))

    dataString = pickle.dumps(packet)
    clientSocketFile.send(dataString)

    print(clientSocketFile.recv(50))

    clientSocketFile.close()


# ip = str(input("Ip Address: "))
ip = socket.gethostname()
port = 1234

answer = str(input("Connect: "))
if answer.upper() == "Y":
    packet = PacketPlayer.PacketPlayer(True)
    sentPacket(ip, port, packet)
