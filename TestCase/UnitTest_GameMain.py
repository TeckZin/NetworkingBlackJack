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


    def test_CheckValue(self):
        print("\033[92mRunning Test ->CheckValue")
        self.assertEqual([8], Test.calculateValue(['4s', '4s']))
        self.assertEqual([6, 16], Test.calculateValue(['1s', '5s']))

        self.assertEqual([3, 13, 23, 33], Test.calculateValue(['1s', '1s', '1s']))
        self.assertEqual([15, 25], Test.calculateValue(['1s', '4s', '11s']))


    def test_CheckGetCardValue(self):
        print("\033[92mRunning Test ->CheckGetCardValue")
        self.assertEqual(3, Test.getCardValue(0, ["3s"]))
        self.assertEqual(4, Test.getCardValue(0, ["4s"]))
        self.assertEqual(10, Test.getCardValue(1, ["3s", "11s"]))
        self.assertEqual(1,  Test.getCardValue(0, ["1s"]))
        self.assertEqual(10, Test.getCardValue(0, ["11s", "13s"]))

if __name__ == '__main__':
    unittest.main()
