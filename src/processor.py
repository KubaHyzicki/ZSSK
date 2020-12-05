from importlib import import_module
from time import sleep
import logging

from src.strategies import *

class Processor():
    def __init__(self, id, tasks_list, strategy, arbitrationRule, expropriation = True):
        self.id = id
        self.tasks = tasks_list
        self.selectStrategy(strategy)
        self.selectArbitrationRule(arbitrationRule)
        self.expropriation = expropriation

        self.task = None

    def selectStrategy(self, strategy):
        try:
            module = import_module("src.strategies.{}".format(strategy))
            self.strategy = getattr(module, strategy.title())(self.tasks)
        except (AttributeError, ImportError):
            logging.error("Selected strategy could not be loaded! Exiting...")
            exit(1)

    def selectArbitrationRule(self, arbitrationRule):
        try:
            module = import_module("src.arbitrationRules.{}".format(arbitrationRule))
            self.arbitrationRule = getattr(module, arbitrationRule.title())(self.tasks)
        except (AttributeError, ImportError) as e:
            print(e)
            logging.error("Selected arbitration rule could not be loaded! Exiting...")
            exit(1)


    def run(self):
        if not self.task:
            self.task = self.choose()
            if not self.task:
                logging.debug("Processor {} could not find any task to proceed".format(self.id))
            else:
                logging.debug("Processor {}: proceeding with task {}".format(self.id, self.task.id))
                self.task.switch_state()

    def stop(self):
        if self.task:
            if self.expropriation or self.task.isDone:
                self.task.switch_state()
                self.task = None

    def choose(self):
        chosen_tasks = self.strategy.choose(self.tasks)
        if len(chosen_tasks) > 1:
            return self.arbitrationRule.choose(chosen_tasks)
        elif len(chosen_tasks) == 1:
            return chosen_tasks[0]
        else:
            return False
