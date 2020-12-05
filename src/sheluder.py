import logging
import threading
from random import randrange
from time import sleep

from src.task import Task
from src.processor import Processor

logging.basicConfig(level = "INFO")

class Sheluder():
    def __init__(self, strategy, arbitration, expropriation, timeChunk, tasks_amount, processors_amount, durations, randomize_durations):
        self.stopper = threading.Event()
        self.strategy = strategy
        self.arbitration = arbitration
        self.expropriation = expropriation
        self.timeChunk = timeChunk
        self.generate_tasks(tasks_amount, durations, randomize_durations)
        self.generate_processors(processors_amount)

    def generate_tasks(self, tasks_amount, durations, randomize_durations):
        self.tasks = []
        if randomize_durations:
            min, max = durations
            for i in range(0, tasks_amount):
                self.tasks.append(Task(id = i,
                    duration = randrange(min, max, 1),
                    stopper = self.stopper))
            return tasks
        else:
            if not tasks_amount == len(durations):
                logging.error("Tasks amount does not match durations list")
                exit(1)
            for i in range(0, tasks_amount):
                self.tasks.append(Task(id = i,
                    duration = durations[i],
                    stopper = self.stopper))

    def generate_processors(self, processors_amount):
        self.processors = []
        for i in range(0, processors_amount):
            self.processors.append(Processor(id = i,
                tasks_list = self.tasks,
                strategy = self.strategy,
                arbitrationRule = self.arbitration,
                expropriation = self.expropriation))

    def run(self):
        #Starting tasks
        for task in self.tasks:
            task.start()

        #Main loop
        try:
            while True:
                for processor in self.processors:
                    processor.run()
                sleep(self.timeChunk)
                for task in self.tasks:
                    task.time_tick()
                for processor in self.processors:
                    processor.stop()
        except KeyboardInterrupt:
            print()
            logging.info("Interrupted. Safety exiting...")
            pass

        #End program
        self.stopper.set()
        self.stopper.clear()
        for task in self.tasks:
            task.join()
