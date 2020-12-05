#arbitration rule - selects first task that whas queued in FIFO order

from operator import itemgetter

from src.arbitrationRules.arbitrationRule import ArbitrationRule

class Chronological(ArbitrationRule):
    def choose(self, tasks):
        timeWaiting = {}
        for index, task in enumerate(tasks):
            timeWaiting[index] = task.currentStateTime
        return tasks[max(timeWaiting.items(), key=itemgetter(1))[0]]
