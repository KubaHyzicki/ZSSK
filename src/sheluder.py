import logging
import threading
from random import randrange
from time import sleep

from src.task import Task
from src.processor import Processor

logging.basicConfig(level = "INFO")

class Sheluder():
    def __init__(self, tasks_amount, processors_amount, durations, randomize_durations):
        self.stopper = threading.Event()
        self.generate_tasks(tasks_amount, durations, randomize_durations)
        self.generate_processors(processors_amount)

    def generate_tasks(self, tasks_amount, durations, randomize_durations):
        self.tasks = []
        if randomize_durations:
            min, max = durations
            for i in range(0, tasks_amount):
                task = Task(id = i, duration = randrange(min, max, 1), stopper = self.stopper)
                self.tasks.append(task)
            return tasks
        else:
            if not tasks_amount == len(durations):
                logging.error("Tasks amount does not match durations list")
                exit(1)
            for i in range(0, tasks_amount):
                task = Task(id = i, duration = durations[i], stopper = self.stopper)
                self.tasks.append(task)

    def generate_processors(self, processors_amount):
        self.processors = []
        for i in range(0, processors_amount):
            self.processors.append(Processor(i, self.tasks))

    def run(self):
        for task in self.tasks:
            task.start()
            logging.info("Task {} started. Duration {}".format(task.id, task.duration))

        #main loop
        try:
            while True:
                for processor in self.processors:
                    processor.run()
                sleep(1)
                for processor in self.processors:
                    processor.stop()
        except KeyboardInterrupt:
            logging.info("Interrupted. Safety exiting...")
            pass

        self.stopper.set()
        self.stopper.clear()
        for task in self.tasks:
            task.join()
