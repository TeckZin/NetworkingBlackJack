from math import floor

import random as random
import Player


class Game:
    houses = ["D", "C", "H", "S"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = []
    playerList = []

    def __init__(self, amountPlayers):
        self.GenerateDeck()
        self.GeneratePlayer(amountPlayers)
        self.GeneratePlayerDeck()

    def GeneratePlayer(self, amountPlayers):
        house = Player.Player(0, True)
        self.playerList.append(house)
        for i in range(amountPlayers):
            player = Player.Player(i + 1, False)
            self.playerList.append(player)


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
                player.addCard(card)
                # print(player.getPlayerDeck(), player.getPlayerNumber())

    def resetHand(self, player):
        player.setPlayerDeck([])
        for i in range(2):
            player.addCard(self.GenerateCard())

    def checkWinner(self, playerList):
        currentWinnter = None
        for x in playerList:
            value = 0
            lst = x.calculateValue()
            for y in lst:
                if value < y <= 21:
                    value = y
                    currentWinnter = x
        print("\33[4mWinnner is player " + str(currentWinnter.getPlayerNumber()) + "\33[0m")



    def GenerateCard(self):
        card = self.deck.pop()
        return card




    def getPlayersList(self):
        return self.playerList

    def printDeck(self):
        print(self.deck)


    def printAllPlayers(self):
        print(self.playerList)



