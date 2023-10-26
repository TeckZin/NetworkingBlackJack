import Game

game = Game.Game(4)
def hitOrStand(playerNumber, strike):
    if(strike == 3):
        print("STAND")
        return False
    print(f"Your cards player {playerNumber} -> ")
    print(player.getPlayerDeck())
    value = str(input("hit or stand: "))
    if value.upper() == "HIT":
        print("HIT")
        Flag = True
    elif value.upper() == "STAND":
        print("STAND")
        Flag = False
    else:
        print(f"Invalid Strike {strike+1}")
        return hitOrStand(playerNumber, strike + 1)

    return Flag

def calculateValue(player):
    return None


def hit(player):
    card = game.GenerateCard()
    player.addCard(card)



turn = 1

while True:
    playersList = game.getPlayersList()
    for player in playersList:
        playerNumber = player.getPlayerNumber()
        isHouse = player.getHouseFlag()
        hit = hitOrStand(playerNumber, 0)







    turn += 1
    break


