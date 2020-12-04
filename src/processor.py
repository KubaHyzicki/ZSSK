from time import sleep
from threading import Thread

class Processor(Thread):
    def __init__(self, id, tasks_list):
        self.id = id
        self.tasks = tasks_list
        self.stop = False

    def run(self, tasks_list_lock):
        while not self.stop:
            with tasks_list_lock:
                task = self.choose()
                task.switch_state()
            sleep(1)

    def choose(self):
    #choose based on strategy
        for task in self.tasks:                    # <- dummy strategy for implementation tests
            if task.status in ['ready', 'waiting']:
                return task
