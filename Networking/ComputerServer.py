import socket, pickle
from BlackJackGame import GameMain, Player


class ComputerServer():
    playerList = []
    gameStart = False
    gameMain = GameMain

    def __init__(self):
        self.startGame()
        if self.gameStart:
            self.listenToMessage(1235)

    def startGame(self):

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
            self.playerList.append(house)

            while True:
                cs, addr = sockFile.accept()

                print(addr)

                command = cs.recv(1024).decode()
                match command:
                    case "Start":
                        amountOfPlayers += 1
                        self.generatePlayer(amountOfPlayers, addr, 1234)

                cs.send(bytes('Accept', 'utf-8'))
                cs.close()

                answer = str(input("Ready to start: "))

                if answer.upper() == "Y" and 1 <= amountOfPlayers <= 7:
                    self.gameMain = GameMain.GameMain(amountOfPlayers + 1, self.playerList)
                    self.gameStart = True
                    sockFile.close()
                else:
                    print("Player excceeded quit or too less")
                    sockFile.close()

    def generatePlayer(self, playerAmount, ip, port):
        player = Player.Player(False, playerAmount, ip, port)
        self.playerList.append(player)

    def listenToMessage(self, port):
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketServer.bind(('', port))

        while True:
            socketServer.listen(30)
            while True:
                cs, addr = socketServer.accept()

    def getGameMain(self):
        return self.gameMain
