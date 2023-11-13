import socket
from Networking import PlayerClient, PlayerServer

# Comp to player -> port 1234

# player to Comp -> port 1234


ip = socket.gethostname()
# ip = str(input("Enter Ip to connect"))


port = 1234

answer = str(input("Connect: "))
if answer.upper() == "Y":
    PlayerClient.sentPacket("Start")

    PlayerServer.PlayeServer(1234)
