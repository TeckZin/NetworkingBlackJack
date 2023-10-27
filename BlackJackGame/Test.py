import Player
import Game


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


def doubleHandGame(player, game):
    doubleHandList = player.getPlayerTwoHandList()
    for i in range(len(doubleHandList) + 1):
        card = game.GenerateCard()
        doubleHandList.append([player.getCard(0), card])

    doubleHandList.pop(0)
    player.setPlayerTwoHandList(doubleHandList)

    for x in doubleHandList:
        print(x)

    return 0


def doubleHandHitStand(player):
    return 0


player2 = Player.Player(1, False)

player2.addCard("11c")
player2.addCard("11c")
game = Game.Game(2)

x = doubleHandGame(player2, game)

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
