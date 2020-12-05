#dummy arbitration rule for implementation tests

from src.arbitrationRules.arbitrationRule import ArbitrationRule

class Dummy(ArbitrationRule):
    def choose(self, tasks):
        return tasks[0]