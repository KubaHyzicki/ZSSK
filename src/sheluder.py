import logging
from random import randrange

from src.task import Task

logging.basicConfig(level = "INFO")

class Sheluder():
    def __init__(self, tasks_amount, durations, randomize_durations):
        if randomize_durations:
            self.tasks = self.randomize_durations(tasks_amount, durations)
        else:
            self.tasks = self.define_durations(tasks_amount, durations)

    def randomize_durations(self, tasks_amount, durations):
        tasks = []
        min, max = durations
        for i in range(0, tasks_amount):
            tasks.append(Task(id=i, duration=randrange(min, max, 1)))
        return tasks

    def define_durations(self, tasks_amount, durations):
        tasks = []
        if not tasks_amount == len(durations):
            logging.error("Tasks amount does not match durations list")
            exit(1)
        for i in range(0, tasks_amount):
            tasks.append(Task(id=i, duration=durations[i]))
        return tasks

    def run(self):
        for task in self.tasks:
            print(task.duration)
        raise NotImplementedError
