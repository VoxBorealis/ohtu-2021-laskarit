class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""
        match_point = 4

        if self.player1_score >= match_point or self.player2_score >= match_point:
            match_point_score = abs(self.player1_score - self.player2_score)
            if match_point_score == 0:
                score = "Deuce"
                return score
            if match_point_score == 1:
                if self.player1_score > self.player2_score:
                    score = f"Advantage {self.player1_name}"
                else:
                    score = f"Advantage {self.player2_name}"
                return score
            if match_point_score >= 2:
                if self.player1_score > self.player2_score:
                    score = f"Win for {self.player1_name}"
                else:
                    score = f"Win for {self.player2_name}"
                return score

        if self.player1_score == 0:
            score = "Love"
        elif self.player1_score == 1:
            score = "Fifteen"
        elif self.player1_score == 2:
            score = "Thirty"
        elif self.player1_score == 3:
            score = "Forty"
        
        score += "-"
        
        if self.player1_score == self.player2_score:
            score += "All"
            return score
        
        if self.player2_score == 0:
            score += "Love"
        elif self.player2_score == 1:
            score += "Fifteen"
        elif self.player2_score == 2:
            score += "Thirty"
        elif self.player2_score == 3:
            score += "Forty"

        return score
