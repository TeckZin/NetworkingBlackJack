import socket, pickle
from BlackJackGame import PacketPlayer


class PlayeServer():

    def __init__(self, port):
        self.runTCP(port)
        # TCP
        # diff port num


    def runTCP(self, port):
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socketServer.bind(('', port))

        while True:
            socketServer.listen(30)

            while True:
                cs, addr = socketServer.accept()


                # keep writing









