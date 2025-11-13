class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_tied_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_endgame_score()
        else:
            return self._get_running_score()

    def _get_tied_score(self):
        tied_scores = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        return tied_scores.get(self.m_score1, "Deuce")

    def _get_endgame_score(self):
        minus_result = self.m_score1 - self.m_score2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_running_score(self):
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        player1_score = score_names[self.m_score1]
        player2_score = score_names[self.m_score2]
        return f"{player1_score}-{player2_score}"
