from stackManager import StackManager
from queueManager import QueueManager


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    """Using dependency here so that the marketing firm can choose which kind of manager they want to use."""
    """depending on what kind of company the firm sells the sweepstakes to they may want to chose the contest in """
    """different ways. """

    def use_sweepstakes_manager(self):
        try:
            self.manager.push()
            self.manager.pop()
            self.manager.enqueue()
            self.manager.dequeue()
        except:
            print('This is not  a sweepstakes manager.')


def create_sweepstakes(name, start_date, end_date, contestants, prize):
    name = ()
    start_date = ()
    end_date = ()
    contestants = ()
    prize = ()
