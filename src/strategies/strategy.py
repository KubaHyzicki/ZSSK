import logging

class Strategy():
    forExpropriating = False
    forNonExpropriating = False

    def __init__(self, tasks, expropriation):
        self.checkExpropration(expropriation)

    def checkExpropration(self, expropriation):
        if expropriation:
            if self.forExpropriating:
                logging.error("This algorithm is not desined for expropriation mode!")
                exit(1)
        else:
            if self.forNonExpropriating:
                logging.error("This algorithm is not desined for non-expropriation mode!")
                exit(1)


    def choose(self, tasks):
        raise NotImplementedError
