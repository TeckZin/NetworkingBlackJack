import unittest
from BlackJackGame import Player, Game, Test


class TestGameMain(unittest.TestCase):

    def test_DoubleHandSplit(self):
        print("\033[92mRunning Test ->DoubleHandSplit")

        player = Player.Player(False, 1, "", 2222)
        game = Game.Game(1, [player])
        card = player.getCard(0, 0)

        result = Test.doubleHandSplit(player)

        self.assertEqual([[card, '1s'], [card, '1s']], result)



if __name__ == '__main__':
    unittest.main()
