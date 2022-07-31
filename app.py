class Set:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.scores = Score()
    
    def first_players(self):
        self.first = self.first + 1
        self.first.normalize()

    def first_player(self):
        return self.scores.scoreName(self.first)

    def second_players(self):
        self.second = self.second + 1
        self.second.normalize()

    def second_player(self):
        return self.scores.scoreName(self.second)

    def normalize(self):
        if self.first == self.scores.maximum() and self.second == self.scores.maximum():
            self.first = self.first - 1
            self.second = self.second - 1

    def winner(self):
        if self.result(self.first, self.second):
            return 1
        
        if self.result(self.second, self.first):
            return 2

    def result(self, winner, loser):
        return winner>3 and winner-loser >= 2



class Score:
    def __init__(self):
        self.scoreNames = ['0','15','30','40','A']
    
    def scoreName(self, index):
        return self.scoreNames[index]
        
    def maximum(self):
        return 4