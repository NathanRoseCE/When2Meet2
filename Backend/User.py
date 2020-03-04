import numpy as np

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # times needs to a numpy int array for the Schedule
        self.times = np.zeros([7, 18], dtype=int)
    def changeAvailibility(self, day, time):
        self.times[day][time] ^= 1