class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.games = dict['games']
    
    @property
    def points(self):
        """Calculate total points (goals + assists)"""
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:20} {self.goals:2} + {self.assists:2} = {self.points:2}"
