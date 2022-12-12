from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or

def show_matcher_results(stats, matcher):
    for player in stats.matches(matcher):
        print(player)
    print()

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    show_matcher_results(stats, And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )) 

    show_matcher_results(stats, And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    ))

    show_matcher_results(stats, And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    ))

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all), len(stats._players))
    print()

    show_matcher_results(stats, Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    ))

    show_matcher_results(stats, And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    ))

if __name__ == "__main__":
    main()
