import Game

game = Game.Game(2)


def hitOrStand(playerNumber, strike, player):
    if strike == 3:
        print("STAND")
        return False
    allPossibleValue = player.calculateValue()
    print(f"Your cards player {playerNumber} -> ")
    print("all your possible values -> ", end="")
    for x in allPossibleValue:
        flag = player.checkBuss(x)
        if flag:
            print("\033[31m" + str(x) + "\033[0m,", end="")
        elif x == 21:
            print("\033[32m" + str(x) + "\033[0m,", end="")
        else:
            print("\033[0m" + str(x) + "\033[0m,", end="")
    print()
    print(player.getPlayerDeck())
    value = str(input("hit or stand: "))
    if value.upper() == "HIT":
        print("HIT")
        flag = True
    elif value.upper() == "STAND":
        print("STAND")
        flag = False
    else:
        print(f"Invalid Strike {strike + 1}")
        return hitOrStand(playerNumber, strike + 1, player)

    return flag


def houseGame(house, game):
    for x in house.calculateValue():
        if len(house.getPlayerDeck()) == 2 and int(x) == 21:
            print("\33[33mRESET\33[0m")
            house.resetHand()
            return houseGame(house, game)
        print(house.getPlayerDeck())
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
            house.addCard(card)
            return houseGame(house, game)


def hit(player):
    card = game.GenerateCard()
    player.addCard(card)


def doubleHandOption(player, strike):
    if strike == 3:
        print("ASSUMING NO")
        return False
    else:
        answer = str(input("Do you want to split your hands [y/n]: "))
    if answer.upper() == "N":
        return False

    elif answer.upper() == "Y":
        return True
    else:
        return doubleHandOption(player, strike + 1)
def doubleHand(player):
    if not player.playerTwoHands:
        lst = player.getPlayerTwoHandList()

        for i in range(2):
            lst[i].append([player.getCardValue(0)])





turn = 1

playersList = game.getPlayersList()
flagAllPlayerBuss = True
for player in playersList:
    playerNumber = player.getPlayerNumber()
    isHouse = player.getHouseFlag()
    if not isHouse:

        if player.checkDouble():
            doubleHand = doubleHandOption(player, 0)

        if doubleHand:
            doubleHand(player)

        else:
            hit = hitOrStand(playerNumber, 0, player)
            while hit:
                card = game.GenerateCard()
                player.addCard(card)
                print("\033[36m" + card + "\033[0m")
                if player.checkAllBuss():
                    value = player.calculateValue()
                    print(f"\033[31mBUST: {value} \033[0m")
                    break

                hit = hitOrStand(playerNumber, 0, player)

house = playersList[0]

print("\33[101mHOUSES TURN \033[0m")
value = houseGame(house, game)

game.checkWinner(playersList, value)
