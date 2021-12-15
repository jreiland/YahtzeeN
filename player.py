class Player:
    def __init__(self, playerNumber = 1, upperScore = 0, lowerScore = 0, totalScore = 0, allScores = ["??", "??", "??", "??", "??", "??", "??", "??", "??", "??", "??", "??", "??"], alreadyScored = [False, False, False, False, False, False, False, False, False, False, False, False, False]):
        self.playerNumber = playerNumber
        self.upperScore = upperScore
        self.lowerScore = lowerScore
        self.totalScore = totalScore
        self.allScores = ["??", "??", "??", "??", "??", "??", "??", "??", "??", "??", "??", "??", "??"] #use question marks to denote score types not yet attempted
        self.alreadyScored = [False, False, False, False, False, False, False, False, False, False, False, False, False]