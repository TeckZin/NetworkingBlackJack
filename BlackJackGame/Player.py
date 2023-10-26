class Player():
    playerNumber = 0
    playerTurn = False
    playerTwoHands = False
    playerTwoHandsOptions = False

    isHouse = False

    def __init__(self, playerNumber, houseFlag):
        self.playerNumber = playerNumber
        self.isHouse = houseFlag
        self.playerDeck = []
        self.playerTurn = False

    def addCard(self, card):
        self.playerDeck.append(card)

    def getPlayerDeck(self):
        return self.playerDeck

    def getPlayerNumber(self):
        return self.playerNumber

    def getHouseFlag(self):
        return self.isHouse

    def getCardValue(self, index):
        card = self.playerDeck[index]
        number = int(card[:-1])
        if number == 11 or number == 12 or number == 13:
            number = 10
        return number

    def calculateValue(self):
        possibilities = []
        # print(player)

        for i in range(len(self.getPlayerDeck())):
            value = self.getCardValue(i)
            isEmpty = len(possibilities) == 0
            if isEmpty:
                if value == 1:
                    possibilities.append(11)
                possibilities.append(value)
            else:
                for j in range(len(possibilities)):
                    sum1 = possibilities[j]
                    possibilities[j] = sum1 + value
                    if value == 1:
                        possibilities.append(sum1 + 11)

        return possibilities

    def checkDouble(self):
        if len(self.getPlayerDeck()) == 2:
            card1 = str(self.playerDeck[0][:-1])
            card2 = str(self.playerDeck[1][:-1])

            if card1 == card2:
                return True

        return False




    def checkBuss(self, x):
        if x > 21:
            return True
        return False

    def checkAllBuss(self):

        for x in self.calculateValue():
            if not self.checkBuss(x):
                return False

        return True

    def setPlayerDeck(self, playerDeck):
        self.playerDeck = playerDeck

