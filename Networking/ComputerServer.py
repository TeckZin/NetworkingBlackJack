import socket, pickle
from BlackJackGame import Player, GameMain


class ComputerServer():
    playerList = []

    def __init__(self):
        sockFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        port = 1234

        sockFile.bind(('', port))

        print("Listening for connections")
        while True:
            sockFile.listen(30)
            amountOfPlayers = 0

            while True:
                cs, addr = sockFile.accept()

                print(addr)

                dataString = cs.recv(1024)
                packet = pickle.loads(dataString)
                print(packet.hit)
                self.playerList.append(packet)
                cs.send(bytes('Accept', 'utf-8'))
                cs.close()

                answer = str(input("Ready to start: "))
                amountOfPlayers += 1

                if answer.upper() == "Y" and 1 <= amountOfPlayers <= 7:
                    self.startGame(amountOfPlayers)
                    sockFile.close()
                else:
                    print("Player excceeded quit or too less")
                    sockFile.close()

    def startGame(self, amountOfPlayers):
        GameMain.GameMain(amountOfPlayers + 1)
