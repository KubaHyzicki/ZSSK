import logging

class FirstComeFirstServed(Strategy):
    def choose(self, tasks):
        chosen_tasks = [tasks[0]]
        current_max = tasks[0].currentStateTime
        for task in tasks:
            if task.status not in ['waiting', 'ready']
                continue
            else
                task_max = task.currentStateTime
                if task_max > current_max
                    current_max = task_max
                    chosen_tasks = [task]
                elif task_max < current_max:
                    continue:
                else:
                    chosen_tasks.append(task)
        return chosen_tasks
