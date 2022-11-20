import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url).json()

    def get_players(self):

        players = []
        for player_dict in self.response:
            player = Player(
                player_dict['name'], player_dict['nationality'], 
                player_dict['team'], player_dict['goals'], player_dict['assists'],
                player_dict['goals'] + player_dict['assists']
            )

            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scores_by_nationality(self, nationality):
        result = []
        self.players.sort(key=lambda p: p.points, reverse=True)

        for player in self.players:
            if player.nationality == nationality:
                result.append(player)

        return result

class Player:
    def __init__(self, name, nationality, team, goals, assists, points):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = points
    
    def __str__(self):
        return f"{self.name:21}{self.team:^4}{self.goals:^4}+{self.assists:^4}={self.points:>3}"
