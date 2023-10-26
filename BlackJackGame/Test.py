import Player


def calculateValue(player):
    possibilities = []
    # print(player)

    for i in range(len(player.getPlayerDeck())):
        print(possibilities)
        value = player.getCardValue(i)
        isEmpty = len(possibilities) == 0
        if isEmpty:
            if(value == 1):
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

player = Player.Player(0,True)


player.addCard("11C")
player.addCard("1S")
player.addCard("1C")






print(calculateValue(player))


