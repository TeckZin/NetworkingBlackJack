import socket, pickle




class PlayeServer():


    def doubleHandOptionPlayer(self, player):
        allPossibleValue = player.calculateValue(player.getPlayerDeck())
        print(f"Your cards player {player.getPlayerNumber()} -> ")
        print("all your possible values -> ", end="")
        self.printAllValue(allPossibleValue, player)
        answer = str(input("Do you want to split your hands [y/n]: "))

    def printAllValue(self, allPossibleValue, player):
        for x in allPossibleValue:
            flag = player.checkBuss(x)
            if flag:
                print("\033[31m" + str(x) + "\033[0m,", end="")
            elif x == 21:
                print("\033[32m" + str(x) + "\033[0m,", end="")
            else:
                print("\033[0m" + str(x) + "\033[0m,", end="")

    def runTCP(self, port):
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socketServer.bind(('', port))

        while True:
            socketServer.listen(30)

            while True:
                cs, addr = socketServer.accept()

                message = socketServer.recv(30)

                # keep writing

    def __init__(self, port):
        self.runTCP(port)
        # TCP
        # diff port num











