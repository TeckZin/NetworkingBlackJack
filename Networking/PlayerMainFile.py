import socket
from Networking import PlayerClient, PlayerServer

# Comp to player -> port 1234 comp servre 1234

# player to Comp -> port 1235 player server 1235


ip = socket.gethostname()
# ip = str(input("Enter Ip to connect"))


port = 1235

answer = str(input("Connect: "))
if answer.upper() == "Y":
    PlayerClient.sendPacket("Start", ip, 1234)

    PlayerServer.PlayerServer(1235)
