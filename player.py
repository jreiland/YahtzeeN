class Player:
    def __init__(self, playerNumber = 1, upperScore = 0, lowerScore = 0, totalScore = 0, allScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], alreadyScored = [False, False, False, False, False, False, False, False, False, False, False, False, False]):
        self.playerNumber = playerNumber
        self.upperScore = upperScore
        self.lowerScore = lowerScore
        self.totalScore = totalScore
        self.allScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.alreadyScored = [False, False, False, False, False, False, False, False, False, False, False, False, False]