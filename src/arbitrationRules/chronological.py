#arbitration rule - selects first task that whas queued in FIFO order

from operator import itemgetter

from src.arbitrationRules.arbitrationRule import ArbitrationRule

class Chronological(ArbitrationRule):
    def choose(self, tasks):
        timeWaiting = {}
        for index, task in enumerate(tasks):
            if task.status == "waiting":
                timeWaiting[index] = task.time_waiting
            if task.status == "ready":
                timeWaiting[index] = task.time_ready
        return tasks[max(timeWaiting.items(), key=itemgetter(1))[0]]
