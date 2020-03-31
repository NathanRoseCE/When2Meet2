import numpy as np
import Hours

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.userHours = Hours.Hours()
        self.userDeviantHours = Hours.Hours()
        self.times = self.userHours.times
        # times needs to a numpy int array for the Schedule

    def changeAvailibility(self, day, time):
        self.userHours.changeAvailibility(day, time)

    def save(self):
        self.userHours.save()

    def load(self, name):
        self.userHours.load(name)


