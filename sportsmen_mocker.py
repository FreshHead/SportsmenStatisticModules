from sport_statistic_lib.sportsman import *


class SportsmenMocker():
    def __init__(self):
        self.sportsmen_list = list()

    def execute(self):
        self.sportsmen_list.append(Sportsman("Иванов", "Ш", 105))
        self.sportsmen_list.append(Sportsman("Петров", "A", 106.3))
