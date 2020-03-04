import numpy as np
import User


class Schedule:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.times = np.zeros([7, 18], dtype=int)
        self.members = []

    def addMember(self, member):
        self.members.append(member)

    def removeMember(self, member):
        self.members.remove(member)

    def calculateTimes(self):
        # reset times
        self.times = np.zeros([7, 18], dtype=int)

        # For each user
        for member in self.members:
            # get the times they are available and add it to the overall time
            self.times += member.times

    def membersAtTime(self, day, time):
        availableMembers = [];
        # for each member
        for member in self.members:
            # see if they are available and if they are add them to the list
            if member[day][time] != 0:
                availableMembers.append(member)

    def membersAtTime(self, timeArray):
        availableMembers = [];
        # for each member
        for member in self.members:
            # see if they are available and if they are add them to the list
            if member.times[timeArray[0]][timeArray[1]] != 0:
                availableMembers.append(member)
        return availableMembers

    def findBestTime(self):
        bestTimes = [[0, 0]]
        mostPeople=0
        for day in range(self.times.shape[0]):
            for time in range(self.times[day].shape[0]):
                if mostPeople < self.times[day, time]:
                    bestTimes = [[day, time]]
                    mostPeople = self.times[day, time]
                elif mostPeople == self.times[day, time]:
                    bestTimes.append([day, time])
        return bestTimes
