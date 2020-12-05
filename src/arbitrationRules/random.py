#arbitration rule - selects random task

from random import choice

from src.arbitrationRules.arbitrationRule import ArbitrationRule

class Random(ArbitrationRule):
    def choose(self, tasks):
        return choice(tasks)