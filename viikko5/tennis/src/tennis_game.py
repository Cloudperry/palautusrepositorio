class Score:
    def __init__(self) -> None:
        self.num = 0

    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3

    def __str__(self) -> str:
        match self.num:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"
            case _:
                return "Over forty"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = Score()
        self.player2_score = Score()

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score.num += 1
        else:
            self.player2_score.num += 1

    def get_score(self):
        if self.player1_score.num == self.player2_score.num:
            if self.player1_score.num <= Score.Forty:
                return f"{self.player1_score}-All"
            else:
                return "Deuce"
        elif self.player1_score.num > Score.Forty or self.player2_score.num > Score.Forty:
            score_diff = self.player1_score.num - self.player2_score.num

            if score_diff == 1:
                return "Advantage player1"
            elif score_diff == -1:
                return "Advantage player2"
            elif score_diff >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
        else:
            return f'{self.player1_score}-{self.player2_score}'
