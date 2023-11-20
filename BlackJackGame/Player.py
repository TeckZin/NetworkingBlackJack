class Player():
    playerNumber = 0
    playerTurn = False
    playerTwoHands = False
    playerTwoHandList = [[]]

    playerDeck = None

    houseFlag = False

    ip = str
    port = int

    def __init__(self, houseFlag, playerNumber, ip, port):
        self.playerNumber = playerNumber
        self.ip = ip
        self.port = port
        self.houseFlag = houseFlag
        self.playerDeck = []
        self.playerTurn = False




    def getIp(self):
        return self.ip

    def getPort(self):
        return self.port

    def setPlayerNumber(self, playerNumber):
        self.playerNumber = playerNumber



    def addCard(self, card, lstIdx):
        if lstIdx == 0:
            self.playerDeck.append(card)
        else:
            self.playerTwoHandList[lstIdx - 1].append(card)

    def getPlayerDeck(self, lstIdx):
        if lstIdx == 0:
            return self.playerDeck
        else:
            return self.playerTwoHandList[lstIdx - 1]

    def getPlayerNumber(self):
        return self.playerNumber

    def getHouseFlag(self):
        return self.houseFlag

    def getCard(self, index, lstIdx):
        if lstIdx == 0:
            return self.playerDeck[index]
        else:
            lst = self.playerTwoHandList[lstIdx - 1]
            return lst[index]

    def getCardValue(self, index, lst):
        card = lst[index]
        number = int(card[:-1])
        if number == 11 or number == 12 or number == 13:
            number = 10
        return number

    def getPlayerTwoHandList(self):
        return self.playerTwoHandList

    def setPlayerTwoHandList(self, lst):
        self.playerTwoHandList = lst

    def calculateValue(self, lst):
        possibilities = []
        # print(player)

        for i in range(len(lst)):
            value = self.getCardValue(i, lst)
            isEmpty = len(possibilities) == 0
            if isEmpty:
                if value == 1:
                    if 11 not in possibilities:
                        possibilities.append(11)
                if value not in possibilities:

                    possibilities.append(value)
            else:
                for j in range(len(possibilities)):

                    sum1 = possibilities[j]

                    possibilities[j] = sum1 + value
                    if value == 1:
                        if sum1 + 11 not in possibilities:
                            print(sum1+11)
                            possibilities.append(sum1 + 11)
        possibilities.sort()
        newLst = []
        [newLst.append(x) for x in possibilities if x not in newLst]
        possibilities = newLst
        return possibilities


    def checkDouble(self):
        if len(self.getPlayerDeck(0)) == 2:
            card1 = str(self.playerDeck[0][:-1])
            card2 = str(self.playerDeck[1][:-1])

            if card1 == card2:
                return True

        return False

    def checkBestCard(self, lst):
        idx = 0
        value = 0
        for x in self.calculateValue(lst):
            if idx == 0:
                value = x
            else:
                if value < x <= 21:
                    value = x

            idx += 1
        return value

    def checkBuss(self, x):
        if x > 21:
            return True
        return False

    def checkAllBuss(self, lst):

        for x in self.calculateValue(lst):
            if not self.checkBuss(x):
                return False

        return True

    def setPlayerDeck(self, playerDeck):
        self.playerDeck = playerDeck
