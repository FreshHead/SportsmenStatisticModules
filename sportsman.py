class Sportsman():
    def __init__(self, surname, team_code, score):
        self.surname = surname
        self.team_code = team_code
        self.score = score
        self.place = None

    def get_tuple(self):
        return [self.surname, self.team_code, self.score, self.place]

    def __getitem__(self, index):
        return self.score