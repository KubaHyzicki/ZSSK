#arbitration rule - selects tasks in cycle which simply means that they are ordered by ID

import logging

from src.arbitrationRules.arbitrationRule import ArbitrationRule

class Cycle(ArbitrationRule):
    def __init__(self, tasks):
        self.queue = [task.id for task in tasks]

    def choose(self, tasks):
        available_ids = []
        for task in tasks:
            available_ids.append(task.id)
        for id in self.queue:
            if id in available_ids:
                self.queue.remove(id)
                self.queue.append(id)
                for task in tasks:
                    if task.id == id:
                        return task
            else:
                continue
        logging.error("Could not find any object from queue!")
        exit(1)
