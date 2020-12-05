import logging

from src.strategies.strategy import Strategy

class LastComeFirstServed(Strategy):
    forExpropriating = True

    def choose(self, tasks):
        chosen_tasks = [tasks[0]]
        current_min = tasks[0].currentStateTime
        for task in tasks:
            if task.status not in ['waiting', 'ready']:
                continue
            else:
                task_min = task.currentStateTime
                if task_min < current_min:
                    current_min = task_min
                    chosen_tasks = [task]
                elif task_min > current_min:
                    continue
                else:
                    chosen_tasks.append(task)
        return chosen_tasks
