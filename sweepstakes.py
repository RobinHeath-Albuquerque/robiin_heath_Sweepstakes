import random
from contenstant import Contestant


class Sweepstakes:
    def __init__(self, name):
        self.name = name

    contestants = {
        "first name": "",
        "last name": "",
        "email": "",
        "registration number": ''
    }

    @classmethod
    def register_contestant(cls):
        self = "registration number"
        print("This contestant has been registered")

    def pick_winner(self, contestant):
        self.pick_winner()
        print(random.choice(contestant))

    def print_contestant_info(self, contestant):
        contestant.print_contestant_info(contestant)


class WinnerMessage:
    print("Congratulations! You Won!")


class NotaWinnerMessage:
    print("Congratulations to " + () + "Please play again!")
