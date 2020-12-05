#dummy strategy for implementation tests

from src.strategies.strategy import Strategy

class Dummy(Strategy):
    def choose(self, tasks):
        chosen_tasks = []
        for task in tasks:
            if task.status in ['ready', 'waiting']:
                chosen_tasks.append(task)
        return chosen_tasks
