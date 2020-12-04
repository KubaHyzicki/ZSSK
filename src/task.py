statuses = ['ready', 'waiting', 'ongoing']

class Task():
    def __init__(self, id, run_time, priority = 0):
        self.status = 'ready'
        self.id = id
        self.run_time
        self.priority = priority

        self.time_waiting = 0
        self.time_ready = 0
        self.time_ongoing = 0

    @property
    def time_until_finish(self):
        if status in ['ongoing', 'waiting']:
            return run_time - time_ongoing
        else return False

    def switch_state(self):
        if status == 'ready':
            status = 'ongoing'
            time_ready = 0
        elif status = 'ongoing':
            if self.time_until_finish == 0:
                status = 'ready'
                time_ongoing = 0
            else:
                status = 'waiting'
        elif status = 'waiting':
            status = 'ongoing'
            time_waiting = 0

    def time_tick(self):
        if status == 'ready':
            time_ready += 1
        elif status = 'ongoing':
            time_ongoing += 1
        elif status = 'waiting':
            time_waiting += 1
