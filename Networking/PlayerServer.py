import socket
from Networking import PlayerClient


class PlayeServer():

    def hitOrStand(self, strike):
        if strike == 3:
            return "False"
        value = str(input("hit or stand: "))
        if value.upper() == "HIT":
            print("HIT")
            return "True"
        elif value.upper() == "STAND":
            print("STAND")
            return "False"
        else:
            print(f"Invalid Strike {strike + 1}")
            return self.hitOrStand(strike + 1)

    def runTCP(self, port):
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socketServer.bind(('', port))

        while True:
            socketServer.listen(30)

            while True:
                cs, addr = socketServer.accept()

                message = socketServer.recv(30)

                message = message.decode("utf-8")

                match message:
                    case "HitStand":
                        PlayerClient.sendPacket(self.hitOrStand(1), addr, port)
                        cs.close()
                        break


                        # keep writing

    def __init__(self, port):
        self.runTCP(port)
        # TCP
        # diff port num
