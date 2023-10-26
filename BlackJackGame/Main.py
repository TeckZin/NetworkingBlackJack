import Game

game = Game.Game(4)


def hitOrStand(playerNumber, strike, player):
    if (strike == 3):
        print("STAND")
        return False
    allPossibleValue = calculateValue(player)
    print(f"Your cards player {playerNumber} -> ")
    print("all your possible values")
    for x in allPossibleValue:
        print(x)
    print(player.getPlayerDeck())
    value = str(input("hit or stand: "))
    if value.upper() == "HIT":
        print("HIT")
        Flag = True
    elif value.upper() == "STAND":
        print("STAND")
        Flag = False
    else:
        print(f"Invalid Strike {strike + 1}")
        return hitOrStand(playerNumber, strike + 1)

    return Flag


def calculateValue(player):
    possibilities = []
    # print(player)
    len1 = len(player.getPlayerDeck())

    for i in range(len1):
        value = player.getCardValue(i)
        isEmpty = len(possibilities) == 0
        if isEmpty:
            if(value == 1):
                possibilities.append(11)
            possibilities.append(value)
        else:
            for j in range(len(possibilities)):
                sum1 = possibilities[j]
                possibilities[j] = sum1 + value
                if value == 1:
                    possibilities.append(sum1 + 11)

    return possibilities


def hit(player):
    card = game.GenerateCard()
    player.addCard(card)


turn = 1

while True:
    playersList = game.getPlayersList()
    for player in playersList:
        playerNumber = player.getPlayerNumber()
        isHouse = player.getHouseFlag()

        hit = hitOrStand(playerNumber, 0, player)

    turn += 1
    break
