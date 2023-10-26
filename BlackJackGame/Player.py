class Player():
    playerNumber = 0
    playerTurn = False
    playerDeck = []
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
        return number

