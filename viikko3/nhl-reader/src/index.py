from player import Player, PlayerReader, PlayerStats

def main():
    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2021-22/players")
    stats = PlayerStats(reader)
    players = stats.top_scores_by_nationality("FIN")

    print(f"Players from FIN:")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
