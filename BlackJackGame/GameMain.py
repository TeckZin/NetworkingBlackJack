import Game
from Networking import ComputerServer
class GameMain():
    def __init__(self, amountOfPlayers):
        game = Game.Game(amountOfPlayers)

        playersList = game.getPlayersList()
        for player in playersList:
            isHouse = player.getHouseFlag()
            if not isHouse:

                if player.checkDouble():
                    flagDouble = self.doubleHandOption(player, 0)
                    if flagDouble:
                        self.doubleHandHitStand(player, game)
                    else:
                        self.hitCard(player, game, 0)

                else:
                    self.hitCard(player, game, 0)

        house = playersList[0]

        print("\33[101mHOUSES TURN \033[0m")
        value = self.houseGame(house, game)

        game.checkWinner(playersList, value)

    def printAllValue(self, allPossibleValue, player):
        for x in allPossibleValue:
            flag = player.checkBuss(x)
            if flag:
                print("\033[31m" + str(x) + "\033[0m,", end="")
            elif x == 21:
                print("\033[32m" + str(x) + "\033[0m,", end="")
            else:
                print("\033[0m" + str(x) + "\033[0m,", end="")


    def hitOrStand(self, playerNumber, strike, player, lstIdx):
        if strike == 3:
            print("STAND")
            return False
        allPossibleValue = player.calculateValue(player.getPlayerDeck(lstIdx))
        print(f"Your cards player {playerNumber} -> ")
        print("all your possible values -> ", end="")
        self.printAllValue(allPossibleValue, player)


        print()
        print(player.getPlayerDeck(lstIdx))
        value = str(input("hit or stand: "))
        if value.upper() == "HIT":
            print("HIT")
            flag = True
        elif value.upper() == "STAND":
            print("STAND")
            flag = False
        else:
            print(f"Invalid Strike {strike + 1}")
            return self.hitOrStand(playerNumber, strike + 1, player, lstIdx)

        return flag


    def houseGame(self, house, game):
        for x in house.calculateValue(house.getPlayerDeck(0)):
            if len(house.getPlayerDeck(0)) == 2 and int(x) == 21:
                print("\33[33mRESET\33[0m")
                house.resetHand()
                return self.houseGame(house, game)
            print(house.getPlayerDeck(0))
            if int(x) >= 17:
                if int(x) == 21:
                    print("\033[32m" + str(x) + "\033[0m")
                elif int(x) > 21:
                    print("\033[31m" + str(x) + "\033[0m")
                else:
                    print("\033[34m" + str(x) + "\033[0m")
                return x
            else:
                card = game.GenerateCard()
                house.addCard(card, 0)
                return self.houseGame(house, game)




    def doubleHandOption(self, player, strike):
        if strike == 3:
            print("ASSUMING NO")
            return False
        else:
            allPossibleValue = player.calculateValue(player.getPlayerDeck())
            print(f"Your cards player {player.getPlayerNumber()} -> ")
            print("all your possible values -> ", end="")
            self.printAllValue(allPossibleValue, player)
            answer = str(input("Do you want to split your hands [y/n]: "))
        if answer.upper() == "N":
            return False

        elif answer.upper() == "Y":
            return True
        else:
            return self.doubleHandOption(player, strike + 1)


    def doubleHandSplitsel (self, player, game):
        doubleHandList = player.getPlayerTwoHandList()
        for i in range(len(doubleHandList) + 1):
            card = game.GenerateCard()
            doubleHandList.append([player.getCard(0,0), card])

        doubleHandList.pop(0)
        player.setPlayerTwoHandList(doubleHandList)
        print(doubleHandList)
        self.doubleHandHitStand(player, game)


    def doubleHandHitStand(self, player, game):
        print("You have two hands")
        doubleHandList = player.getPlayerTwoHandList()
        idx = 1
        for x in doubleHandList:
            print(f"your {idx} hand: ")
            print(x)
            self.hitCard(player, game, idx)
            idx += 1


    def hitCard(self, player, game, lstIdx):
        playerNumber = player.getPlayerNumber()
        hitFlag = self.hitOrStand(playerNumber, 0, player, lstIdx)
        while hitFlag:
            card = game.GenerateCard()
            player.addCard(card, lstIdx)
            print("\033[36m" + card + "\033[0m")
            if player.checkAllBuss(player.getPlayerDeck(lstIdx)):
                value = player.calculateValue(player.getPlayerDeck(lstIdx))
                print(f"\033[31mBUST: {value} \033[0m")
                return True

            hitFlag = self.hitOrStand(playerNumber, 0, player, lstIdx)






