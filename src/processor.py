from time import sleep
import logging

class Processor():
    def __init__(self, id, tasks_list):
        self.id = id
        self.tasks = tasks_list
        self.task = None

    def run(self):
        self.task = self.choose()
        if not self.task:
            logging.warning("Processor {} could not find any task to proceed".format(self.id))
        else:
            self.task.switch_state()

    def stop(self):
        if self.task:
            self.task.switch_state()
            self.task = None


    def choose(self):
    #choose based on strategy
        for task in self.tasks:                    # <- dummy strategy for implementation tests
            if task.status in ['ready', 'waiting']:
                return task
        return False
