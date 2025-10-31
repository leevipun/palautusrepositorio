class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
        self.team = player_dict['team']
        self.nationality = player_dict['nationality']
        self.games = player_dict['games']

    @property
    def points(self):
        """Calculate total points (goals + assists)"""
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:20} {self.goals:2} + {self.assists:2} = {self.points:2}"
