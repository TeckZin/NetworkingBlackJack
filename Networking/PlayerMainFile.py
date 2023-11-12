import socket
from BlackJackGame import PacketPlayer, Player
from Networking import PlayerClient, PlayerServer


#Comp to player -> port 1234

#player to Comp -> port 1235



ip = socket.gethostname()
# ip = str(input("Enter Ip to connect"))


port = 1234

answer = str(input("Connect: "))
if answer.upper() == "Y":
    packet = Player.Player(False, ip, port)
    playerClient = PlayerClient.PlayerClient(ip, port)
    playerClient.sentPacket(packet)

    PlayerServer.PlayeServer(1235, gameMain)


