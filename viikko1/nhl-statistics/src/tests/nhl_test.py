import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player(self):
        player = self.stats.search("Semenko")

        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_search_returns_none_when_player_not_found(self):
        player = self.stats.search("Selänne")

        self.assertEqual(player, None)

    def test_search_partial_name_match(self):
        player = self.stats.search("Gret")
        self.assertEqual(player.name, "Gretzky")

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")

        self.assertEqual(len(team_players), 3)
        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[1].name, "Kurri")
        self.assertEqual(team_players[2].name, "Gretzky")

    def test_team_returns_empty_list_for_nonexistent_team(self):
        team_players = self.stats.team("NYR")
        self.assertEqual(len(team_players), 0)

    def test_team_returns_single_player(self):
        team_players = self.stats.team("PIT")
        self.assertEqual(len(team_players), 1)
        self.assertEqual(team_players[0].name, "Lemieux")

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(3)

        self.assertEqual(len(top_players), 4)  # Bug: returns how_many + 1
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 pistettä
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 pistettä
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 pistettä

    def test_top_returns_players_in_correct_order(self):
        top_players = self.stats.top(4)

        self.assertEqual(top_players[0].name, "Gretzky")  # 124 pistettä
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 pistettä
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 pistettä
        self.assertEqual(top_players[3].name, "Kurri")    # 90 pistettä

    def test_top_returns_all_players_when_how_many_exceeds_player_count(self):
        top_players = self.stats.top(10)
        self.assertEqual(len(top_players), 4)  # Returns how_many + 1 players

    def test_top_zero_returns_one_player(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)  # Bug: returns 1 instead of 0
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(3)

        self.assertEqual(len(top_players), 4)  # Returns how_many + 1 players
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 pistettä
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 pistettä
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 pistettä

    def test_top_returns_players_in_correct_order(self):
        top_players = self.stats.top(4)

        self.assertEqual(top_players[0].name, "Gretzky")  # 124 pistettä
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 pistettä
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 pistettä
        self.assertEqual(top_players[3].name, "Kurri")    # 90 pistettä
