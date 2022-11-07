import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search(self):
        kurri = self.statistics.search("Kurri")
        self.assertEqual(kurri.name, "Kurri")
        self.assertEqual(kurri.team, "EDM")
        self.assertEqual(kurri.goals, 37)
        self.assertEqual(kurri.assists, 53)

    def test_search_nonexistent(self):
        self.assertEqual(self.statistics.search("Hokkanen"), None)

    def test_team(self):
        # This test should maybe be programmed in a way that it works even if the statistics.team doesn't preserve order
        team = self.statistics.team("EDM")
        self.assertEqual(
            team[0].name, "Semenko"
        )
        self.assertEqual(
            team[1].name, "Kurri" 
        )
        self.assertEqual(
            team[2].name, "Gretzky" 
        )

    def test_top(self):
        top3 = self.statistics.top(3)
        self.assertEqual(top3[0].name, "Gretzky")
        self.assertEqual(top3[1].name, "Lemieux")
        self.assertEqual(top3[2].name, "Yzerman")
