import random as random
from Networking import ClientComputer


class Game():
    houses = ["D", "C", "H", "S"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = []
    playerList = []
    amountPlayers = 0

    def __init__(self, amountPlayers, playerList):
        self.amountPlayers = amountPlayers
        self.playerList = playerList
        self.GenerateDeck()

        self.GeneratePlayerDeck()

        # need soem fixing

    def GenerateDeck(self):
        for i in range(len(self.houses)):
            for j in range(len(self.numbers)):
                self.deck.append(str(self.numbers[j]) + self.houses[i])
        random.shuffle(self.deck)

    def GeneratePlayerDeck(self):
        for i in range(2):
            # print(i)
            for player in self.playerList:
                card = self.GenerateCard()
                # print(card)
                player.addCard(card, 0)
                # print(player.getPlayerDeck(), player.getPlayerNumber())

    def resetHand(self, player):
        player.setPlayerDeck([])
        for i in range(2):
            player.addCard(self.GenerateCard(), 0)

    def checkWinner(self, playerList, houseValue):
        listValue = {}

        output = "RESULT\n"

        houseBuss = False
        for player in playerList:

            value = player.checkBestCard(player.getPlayerDeck(0))
            playerNum = player.getPlayerNumber()

            if playerNum == 0:
                houseBuss = player.checkBuss(value)
            else:
                buss = player.checkBuss(value)
                if not buss and houseBuss:
                    listValue[playerNum] = value

                    ClientComputer.sentMessage(f"Win -> you with value: {value} House buss with: {houseValue}\n",
                                               player.getIp(), player.getPort(), "NONE")
                elif buss and houseBuss:
                    listValue[playerNum] = value
                    ClientComputer.sentMessage(
                        f"Win Both buss -> you with value: {value}, House buss with value {houseValue}\n",
                        player.getIp(), player.getPort(), "NONE")
                elif not buss and not houseBuss:

                    if houseValue > value:
                        listValue[0] = houseValue

                        ClientComputer.sentMessage(
                            f"Lost -> you with value: {value}, House won with value {houseValue}\n", player.getIp(),
                            player.getPort(), "NONE")

                    elif value >= houseValue:

                        listValue[playerNum] = value

                        ClientComputer.sentMessage(
                            f" Win -> you with value: {value}, House lost with value {houseValue}\n", player.getIp(),
                            player.getPort(), "NONE")
                elif buss and not houseBuss:
                    # print("here")
                    listValue[0] = houseValue

                    ClientComputer.sentMessage(
                        f"Lost with buss -> you with value: {value}, House won with value {houseValue}\n",
                        player.getIp(), player.getPort(), "NONE")
        # print("\33[4mWinnner is player ")

        output += "\33[4mWinnner is player \n"
        for player, y in listValue.items():
            # print(f"\33[0m\33[32m{player} with value of {y}")
            output += f"\33[0m\33[32m{player} with value of {y}\n"

        # print("\33[0m")
        output += f"\33[0m\n"
        # print(output)
        return output

    def GenerateCard(self):
        card = self.deck.pop()
        return card

    def getPlayersList(self):
        return self.playerList

    def printDeck(self):
        print(self.deck)

    def printAllPlayers(self):
        print(self.playerList)
