import socket, pickle
from BlackJackGame import PacketPlayer, GameMain, Player


class ComputerServer():
    playerPacketList = []

    def __init__(self):
        global packet
        sockFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        port = 1234

        sockFile.bind(('', port))

        print(socket.gethostname())

        print("Listening for connections")
        while True:
            sockFile.listen(30)
            amountOfPlayers = 0
            house = Player.Player(True, socket.gethostname(), port)
            house.setPlayerNumber(0)
            self.playerPacketList.append(house)

            while True:
                cs, addr = sockFile.accept()

                print(addr)

                dataString = cs.recv(1024)
                amountOfPlayers += 1
                packet.setPlayerNumber(amountOfPlayers)

                packet = pickle.loads(dataString)

                print(packet)



                self.playerPacketList.append(packet)

                cs.send(bytes('Accept', 'utf-8'))
                cs.close()

                answer = str(input("Ready to start: "))


                if answer.upper() == "Y" and 1 <= amountOfPlayers <= 7:
                    self.startGame(amountOfPlayers, self.playerPacketList)
                    sockFile.close()
                else:
                    print("Player excceeded quit or too less")
                    sockFile.close()

    def startGame(self, amountOfPlayers, playerList):
        GameMain.GameMain(amountOfPlayers + 1, playerList)
