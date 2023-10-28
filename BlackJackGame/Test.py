import Player
import Game


def hitCard(player, game, lstIdx):
    playerNumber = player.getPlayerNumber()
    hitFlag = hitOrStand(playerNumber, 0, player, lstIdx)
    while hitFlag:
        card = game.GenerateCard()
        player.addCard(card, lstIdx)
        print("\033[36m" + card + "\033[0m")
        if player.checkAllBuss(player.getPlayerDeck(lstIdx)):
            value = player.calculateValue(player.getPlayerDeck(lstIdx))
            print(f"\033[31mBUST: {value} \033[0m")
            return True

        hitFlag = hitOrStand(playerNumber, 0, player, lstIdx)


def hitOrStand(playerNumber, strike, player, lstIdx):
    if strike == 3:
        print("STAND")
        return False
    allPossibleValue = player.calculateValue(player.getPlayerDeck(lstIdx))
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
        return hitOrStand(playerNumber, strike + 1, player, lstIdx)

    return flag


def calculateValue(player):
    possibilities = []
    # print(player)

    for i in range(len(player.getPlayerDeck())):
        print(possibilities)
        value = player.getCardValue(i)
        isEmpty = len(possibilities) == 0
        if isEmpty:
            if (value == 1):
                possibilities.append(11)
            possibilities.append(value)
        else:
            for j in range(len(possibilities)):

                sum1 = possibilities[j]

                print(sum1)
                possibilities[j] = sum1 + value
                if value == 1:
                    possibilities.append(sum1 + 11)

    return possibilities


def doubleHandSplit(player, game):
    doubleHandList = player.getPlayerTwoHandList()
    for i in range(len(doubleHandList) + 1):
        card = game.GenerateCard()
        doubleHandList.append([player.getCard(0,0), card])

    doubleHandList.pop(0)
    player.setPlayerTwoHandList(doubleHandList)
    print(doubleHandList)
    doubleHandHitStand(player)


def doubleHandHitStand(player):
    print("You have two hands")
    doubleHandList = player.getPlayerTwoHandList()
    idx = 1
    for x in doubleHandList:
        print(f"your {idx} hand: ")
        print(x)
        hitCard(player2, game, idx)
        idx += 1


player2 = Player.Player(1, False)

player2.addCard("11c", 0)
player2.addCard("11c", 0)
game = Game.Game(2)

x = doubleHandSplit(player2, game)

# player = Player.Player(0,True)
#
#
# player.addCard("11C")
# player.addCard("1S")
# player.addCard("1C")
#
#
#
#
#
#
# print(calculateValue(player))
