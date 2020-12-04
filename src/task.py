statuses = ['ready', 'waiting', 'ongoing']

class Task():
    def __init__(self, id, duration, priority = 0):
        self.status = 'ready'
        self.id = id
        self.duration = duration
        self.priority = priority

        self.time_waiting = 0
        self.time_ready = 0
        self.time_ongoing = 0

    @property
    def time_until_finish(self):
        if self.status in ['ongoing', 'waiting']:
            return self.duration - time_ongoing
        else:
            return False

    def switch_state(self):
        if self.status == 'ready':
            self.status = 'ongoing'
            time_ready = 0
        elif self.status == 'ongoing':
            if self.time_until_finish == 0:
                self.status = 'ready'
                time_ongoing = 0
            else:
                self.status = 'waiting'
        elif self.status == 'waiting':
            self.status = 'ongoing'
            time_waiting = 0

    def time_tick(self):
        if self.status == 'ready':
            time_ready += 1
        elif self.status == 'ongoing':
            time_ongoing += 1
        elif self.status == 'waiting':
            time_waiting += 1
