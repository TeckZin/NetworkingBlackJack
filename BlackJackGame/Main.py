import Game

game = Game.Game(4)
game.printDeck()
game.printAllPlayers()

turn = 1

while True:
    playersList = game.getPlayersList()
    for player in playersList:
        playerNumber = player.getPlayerNumber()
        isHouse = player.getHouseFlag()



    turn += 1

