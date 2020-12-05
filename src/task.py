from threading import Thread
import time
import logging

statuses = ['ready', 'waiting', 'ongoing']

class Task(Thread):
    def __init__(self, id, duration, stopper, priority = 0):
        super(Task, self).__init__()
        self.status = 'ready'
        self.id = id
        self.duration = duration
        self.stopper = stopper
        self.priority = priority

        self.current_left = duration

    def run(self):
        logging.info("Starting task {}".format(self.id))
        self.start = Task.get_time()
        self.stopper.wait()

    @property
    def time_until_finish(self):
        if self.status in ['ongoing', 'waiting']:
            return self.current_left - self.time_ongoing
        else:
            return False

    @property
    def time_ongoing(self):
        return Task.get_time() - self.start

    @property
    def time_waiting(self):
        return Task.get_time() - self.start

    @property
    def time_ready(self):
        return Task.get_time() - self.start

    def switch_state(self):
        if self.status == 'ready':
            self.status = 'ongoing'
            logging.info("Switching Task {} state: ready -> ongoing".format(self.id))
        elif self.status == 'waiting':
            self.status = 'ongoing'
            logging.info("Switching Task {} state: waiting -> ongoing".format(self.id))
        elif self.status == 'ongoing':
            #freezing time when check starts as there is "space" between time_until_finish usages
            time_until_finish = self.time_until_finish
            if time_until_finish > 0:
                self.status = 'waiting'
                self.current_left = time_until_finish
                logging.info("Switching Task {} state: ongoing -> waiting ({} left)".format(self.id, time_until_finish))
            else:
                self.status = 'ready'
                self.current_left = self.duration
                logging.info("Switching Task {} state: ongoing -> ready".format(self.id))
        self.start = Task.get_time()

    # def time_tick(self):
    #     if self.status == 'ready':
    #         self.time_ready += 1
    #     elif self.status == 'ongoing':
    #         self.time_ongoing += 1
    #     elif self.status == 'waiting':
    #         self.time_waiting += 1

    @staticmethod
    def get_time():
        return time.clock() * 10000
