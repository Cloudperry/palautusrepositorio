import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []
    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['nationality'], 
            player_dict['team'], player_dict['goals'], player_dict['assists'],
            player_dict['goals'] + player_dict['assists']
        )

        players.append(player)

    print("Players from FIN:")
    players.sort(key=lambda p: p.points, reverse=True)
    for player in players:
        if player.nationality == "FIN":
            print(f"{player.name:21}{player.team:^4}{player.goals:^4}+{player.assists:^4}={player.points:>3}")

if __name__ == "__main__":
    main()
