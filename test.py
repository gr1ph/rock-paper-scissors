import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("Testing game against quincy...")
        actual = play(player, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Player estimated more than 60% of games as winning against quincy')

    def test_player_vs_abbey(self):
        print("Testing game against abbey...")
        actual = play(player, abbey, 1000) >= 60
        self.assertTrue(
            actual,
            'Player estimated more than 60% of games as winning against abbey')

    def test_player_vs_kris(self):
        print("Testing game against kris...")
        actual = play(player, kris, 1000) >= 60
        self.assertTrue(
            actual, 'Player estimated more than 60% of games as winning against kris')

    def test_player_vs_mrugesh(self):
        print("Testing game against mrugesh...")
        actual = play(player, mrugesh, 1000) >= 60
        self.assertTrue(
            actual,
            'Player estimated more than 60% of games as winning against mrugesh')


if __name__ == "__main__":
    unittest.main()