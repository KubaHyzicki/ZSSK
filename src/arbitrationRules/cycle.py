#arbitration rule - selects tasks in cycle which simply means that they are ordered by ID

from src.arbitrationRules.arbitrationRule import ArbitrationRule

class Cycle(ArbitrationRule):
    def __init__(self, tasks):
        queue = list()

    def choose(self, tasks):
        raise NotImplementedError
        return choice(tasks)
