from operator import itemgetter

from sport_statistic_lib.sportsman import *


class SportsmenMocker():
    def __init__(self):
        self.sportsmen_list = list()

    def execute(self):
        self.sportsmen_list.append(Sportsman("Иванов", "Ш", 105))
        self.sportsmen_list.append(Sportsman("Петров", "A", 106.3))
        self.add_place()

    def add_place(self):
        self.sportsmen_list.sort(key=itemgetter(3))
        for i in range(0, len(self.sportsmen_list)):
            self.sportsmen_list[i].place = i + 1
