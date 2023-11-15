from BlackJackGame import Game
from Networking import ClientComputer


class GameMain():
    def __init__(self, amountOfPlayers, playerList):
        game = Game.Game(amountOfPlayers, playerList)

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
        output = ""
        for x in allPossibleValue:
            flag = player.checkBuss(x)
            if flag:
                # print("\033[31m" + str(x) + "\033[0m,", end="")
                output += "\033[31m" + str(x) + "\033[0m,"
            elif x == 21:
                # print("\033[32m" + str(x) + "\033[0m,", end="")
                output += "\033[32m" + str(x) + "\033[0m,"

            else:
                # print("\033[0m" + str(x) + "\033[0m,", end="")
                output += "\033[0m" + str(x) + "\033[0m,"
        print(output)
        return output

    def hitOrStand(self, playerNumber, strike, player, lstIdx, game):

        output = ""
        if strike == 3:
            print("STAND")
            return False
        allPossibleValue = player.calculateValue(player.getPlayerDeck(lstIdx))
        # print(f"Your cards player {playerNumber} -> ")

        output += f"Your cards player {playerNumber} -> \n"

        # print("all your possible values -> ", end="")

        output += "all your possible values -> "

        output += self.printAllValue(allPossibleValue, player)

        output += "\n" + str(player.getPlayerDeck(lstIdx))

        print(output)

        messageFlag = ClientComputer.sentMessage(output, player.getIp(), player.getPort(), "HITORSTAND")
        generalMessage = ""

        if messageFlag == "True":
            generalMessage = output + "HIT"
            ClientComputer.sentToALL(generalMessage, game.getPlayersList(), "NONE")
            return True

        generalMessage = output + "STAND"

        ClientComputer.sentToALL(generalMessage, game.getPlayersList(), "NONE")

        return False

        # get resutlt forom player

    def houseGame(self, house, game):

        output = ""
        for x in house.calculateValue(house.getPlayerDeck(0)):
            if len(house.getPlayerDeck(0)) == 2 and int(x) == 21:
                # print("\33[33mRESET\33[0m")
                output += "\33[33mRESET\33[0m\n"
                house.resetHand()
                return self.houseGame(house, game)
            output += str(house.getPlayerDeck(0))
            if int(x) >= 17:
                if int(x) == 21:
                    # print("\033[32m" + str(x) + "\033[0m")
                    output += "\033[32m" + str(x) + "\033[0m\n"

                elif int(x) > 21:
                    # print("\033[31m" + str(x) + "\033[0m")
                    output += "\033[31m" + str(x) + "\033[0m\n"
                else:
                    # print("\033[34m" + str(x) + "\033[0m")
                    output += "\033[34m" + str(x) + "\033[0m\n"
                print(output)


                ClientComputer.sentToALL(output, game.getPlayersList(), "END")
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

            output = ""
            allPossibleValue = player.calculateValue(player.getPlayerDeck(0))
            # print(f"Your cards player {player.getPlayerNumber()} -> ")

            output += f"Your cards player {player.getPlayerNumber()} -> \n"

            # print("all your possible values -> ", end="")

            output += "all your possible values -> "
            output += self.printAllValue(allPossibleValue, player)
            print(output)

            # send message

            answer = ClientComputer.sentMessage(output, player.getIp(), player.getPort(), "YORN")
            # answer = str(input("Do you want to split your hands [y/n]: "))
            if answer.upper() == "N":
                return False
            elif answer.upper() == "Y":
                return True

    def doubleHandSplit(self, player, game):
        doubleHandList = player.getPlayerTwoHandList()
        for i in range(len(doubleHandList) + 1):
            card = game.GenerateCard()
            doubleHandList.append([player.getCard(0, 0), card])

        doubleHandList.pop(0)
        player.setPlayerTwoHandList(doubleHandList)
        output = str(doubleHandList)
        ClientComputer.sentMessage(output, player.getIp(), player.getPort(),"NONE")
        self.doubleHandHitStand(player, game)

    def doubleHandHitStand(self, player, game):
        output = "You have two hands"
        doubleHandList = player.getPlayerTwoHandList()
        idx = 1
        for x in doubleHandList:
            # print(f"your {idx} hand: ")
            # print(x)

            output += f"your {idx} hand: \n" + str(x) + "\n"
            self.hitCard(player, game, idx)
            idx += 1

        ClientComputer.sentMessage(output, player.getIp(), player.getPort(), "NONE")
        print(output)

    def hitCard(self, player, game, lstIdx):
        playerNumber = player.getPlayerNumber()
        hitFlag = self.hitOrStand(playerNumber, 0, player, lstIdx, game)
        output = ""
        while hitFlag:
            card = game.GenerateCard()
            player.addCard(card, lstIdx)
            # print("\033[36m" + card + "\033[0m")
            output += "\033[36m" + card + "\033[0m"
            if player.checkAllBuss(player.getPlayerDeck(lstIdx)):
                value = player.calculateValue(player.getPlayerDeck(lstIdx))
                # print(f"\033[31mBUST: {value} \033[0m")
                output += f"\033[31mBUST: {value} \033[0m"
                ClientComputer.sentMessage(output, player.getIp(), player.getPort(), "NONE")
                print(output)
                return True

            hitFlag = self.hitOrStand(playerNumber, 0, player, lstIdx, game)
