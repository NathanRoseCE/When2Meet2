import numpy as np


class Hours:
    def __init__(self):
        # Not sure what we need to predefine
        self.times = np.zeros([7, 48], dtype=int)

    def changeAvailibility(self, day, time):
        self.times[day][time] ^= 1

    def save(self):
        saveFile = open(self.name + ".csv", "w")
        saveFile.write(self.name + "," + self.id + ",\n")
        for day in self.times:
            dayLine = ""
            for time in day:
                dayLine = dayLine + str(time) + ","
            saveFile.write(dayLine + "\n")
        saveFile.close()

    def load(self, name):
        loadFile = open(name + ".csv", "r")
        info = loadFile.readline().split(",")
        self.name = info[0]
        self.id = info[1]
        for day in range(int(self.times.size / self.times[0].size)):
            dayTimes = loadFile.readline().split(",")
            for times in range(self.times[day].size):
                self.times[day][times] = dayTimes[times]