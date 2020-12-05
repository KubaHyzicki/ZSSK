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
        self.start_time = 0

        self.current_left = duration

    def run(self):
        logging.info("Starting task {}. Duration {}".format(self.id, self.duration))
        self.start_time = Task.get_time()
        self.stopper.wait()

    @property
    def time_until_finish(self):
        if self.status in ['ongoing', 'waiting']:
            return self.current_left - self.currentStateTime
        else:
            return False

    @property
    def currentStateTime(self):
        return Task.get_time() - self.start_time

    @property
    def isDone(self):
        if self.status in ['ongoing', 'waiting']:
            return self.currentStateTime <= 0
        else:
            return False


    def switch_state(self):
        if self.status == 'ready':
            self.status = 'ongoing'
            logging.debug("Switching Task {} state: ready -> ongoing".format(self.id))
        elif self.status == 'waiting':
            self.status = 'ongoing'
            logging.debug("Switching Task {} state: waiting -> ongoing".format(self.id))
        elif self.status == 'ongoing':
            #freezing time when check starts as there is "space" between time_until_finish usages
            time_until_finish = self.currentStateTime
            if self.isDone:
                self.status = 'ready'
                self.current_left = self.duration
                logging.debug("Switching Task {} state: ongoing -> ready".format(self.id))
            else:
                self.status = 'waiting'
                self.current_left = time_until_finish
                logging.debug("Switching Task {} state: ongoing -> waiting ({} left)".format(self.id, time_until_finish))
        self.start_time = Task.get_time()

    @staticmethod
    def get_time():
        return time.clock() * 10000
        # return int(time.clock() * 10000)      #alternative for more chunky approach
