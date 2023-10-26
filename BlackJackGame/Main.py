import Game

game = Game.Game(4)


def hitOrStand(playerNumber, strike, player):
    if (strike == 3):
        print("STAND")
        return False
    allPossibleValue = player.calculateValue()
    print(f"Your cards player {playerNumber} -> ")
    print("all your possible values -> ", end="")
    for x in allPossibleValue:
        flag = player.checkBuss(x)
        if flag:
            print("" + str(x) + ",", end="")
        print(str(x) + ",", end="")
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
        return hitOrStand(playerNumber, strike + 1)

    return flag






def hit(player):
    card = game.GenerateCard()
    player.addCard(card)


turn = 1

while True:
    playersList = game.getPlayersList()
    flagAllPlayerBuss = True
    for player in playersList:
        playerNumber = player.getPlayerNumber()
        isHouse = player.getHouseFlag()

        hit = hitOrStand(playerNumber, 0, player)
        while hit:
            card = game.GenerateCard()
            player.addCard(card)
            print(card)
            if player.checkAllBuss():
                print("BUSS")
                break

            hit = hitOrStand(playerNumber, 0, player)




    break

