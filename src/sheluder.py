import logging
import threading
from random import randrange
from time import sleep

from src.task import Task
from src.processor import Processor

logging.basicConfig(level = "INFO")

class Sheluder():
    def __init__(self, tasks_amount, processors_amount, durations, randomize_durations):
        self.generate_tasks(tasks_amount, durations, randomize_durations)
        self.generate_processors(processors_amount)

    def generate_tasks(self, tasks_amount, durations, randomize_durations):
        self.tasks = []
        if randomize_durations:
            min, max = durations
            for i in range(0, tasks_amount):
                self.tasks.append(Task(id = i, duration = randrange(min, max, 1)))
            return tasks
        else:
            if not tasks_amount == len(durations):
                logging.error("Tasks amount does not match durations list")
                exit(1)
            for i in range(0, tasks_amount):
                self.tasks.append(Task(id = i, duration = durations[i]))

    def generate_processors(self, processors_amount):
        self.processors = []
        for i in range(0, processors_amount):
            self.processors.append(Processor(i, self.tasks))

    def run(self):
        tasks_list_lock = threading.Lock()
        for task in self.tasks:
            logging.info("Task {}. Duration set to {}".format(task.id, task.duration))
        for processor in self.processors:
            processor.run(tasks_list_lock)

        sleep(10)
        for processor in processors:
            processor.stop = True           #to be changed to event
            processor.join()

        raise NotImplementedError
