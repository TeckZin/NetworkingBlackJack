class Player():
    playerNumber = 0
    playerTurn = False
    playerDeck = []
    isHouse = False

    def __init__(self, playerNumber, houseFlag):
        self.playerNumber = playerNumber
        self.isHouse = houseFlag

    def addCards(self, card):
        self.playerDeck.append(card)


    def getPlayerNumber(self):
        return self.playerNumber

    def getHouseFlag(self):
        return self.isHouse
