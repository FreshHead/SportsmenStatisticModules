from operator import itemgetter

from sport_statistic_lib.sportsman import *

class SportsmenMocker():
    def __init__(self):
        self.sportsmen = list()

    def execute(self):
        self.sportsmen.append(Sportsman("Иванов", "Ш", 105))
        self.sportsmen.append(Sportsman("Петров", "A", 106.3))

    def add_place(self):
        self.sportsmen.sort(key=itemgetter(3))
        for i in range(0, len(self.sportsmen)):
            self.sportsmen[i].place(i + 1)
