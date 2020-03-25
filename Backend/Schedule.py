import numpy as np
import User
import TimeChunk


class Schedule:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.times = np.zeros([7, 48], dtype=int)
        self.members = []
        self.critical = []

    def addMember(self, member, critical):
        self.members.append(member)
        self.critical.append(critical)

    #untested
    def removeMember(self, memberId):
        for i in range(self.members):
            if self.member[i].id == memberId:
                self.members.remove(self.members[i])
                self.critical.remove(self.critical[i])


    def calculateTimes(self):
        # reset times
        self.times = np.zeros([7, 48], dtype=int)

        # For each user
        for member in self.members:
            # get the times they are available and add it to the overall time
            self.times += member.times

    def membersAtTime(self, day, time):
        availableMembers = []
        # for each member
        for member in self.members:
            # see if they are available and if they are add them to the list
            if member[day][time] != 0:
                availableMembers.append(member)

    def membersAtTime(self, timeArray):
        availableMembers = []
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

    def determineBestMeetingTime(self):
        criticalMembers = []
        nonCriticalMembers = []
        for i in range(len(self.members)):
            if self.critical[i] == True:
                criticalMembers.append(self.members[i])
            else:
                nonCriticalMembers.append(self.members[i])

        # determine chunks
        chunks = TimeChunk.determineAllChunks(self.members)

        # Determine times when all critical members can meet
        criticalChunks = [];
        for chunk in chunks:
            allCritical = True
            for criticalMember in criticalMembers:
                if chunk.members.count(criticalMember) == 0:
                    allCritical = False
                    break
            if allCritical:
                criticalChunks.append(chunk)

        if criticalChunks == []:
            print("Not all critical members can meet")
            print("Suggested to remove some members")
            return []

        # make sure every member can meet at the restricted time of only critical members
        nonCriticalCopy = nonCriticalMembers.copy()
        for chunk in criticalChunks:
            for member in chunk.members:
                #I know I should specify the error but Im a bit lazy rn and this is the only erro that should occur
                try:
                    nonCriticalCopy.remove(member)
                except:
                    i = 0# throwaway line

        # If they cant print a message and list all names
        if len(nonCriticalCopy) != 0:
            print("The following members are not able to meet due to critical member hours, and have been removed")
            for member in nonCriticalCopy:
                nonCriticalMembers.remove(member)
                print(member.name)

        # This is where the fun begins, determining the best time to meet
        # This is done through recursion, a dummy node is placed at the front
        # because its the most elegant solution I found to make this iterate through all of them
        solutionSet = []
        if nonCriticalMembers == []:
            for chunk in criticalChunks:
                solutionSet.append([chunk])

        depth = 0
        dummyHead = TimeChunk.TimeChunk([-1,-1],[-1,-1], [])
        criticalChunks.insert(0, dummyHead)
        while solutionSet == []:
            depth = depth + 1
            resultSet = findMeetingTime(criticalChunks.copy(), nonCriticalMembers.copy(), depth)
            if resultSet != []:
                # remove dummy node
                for result in resultSet:
                    del result[0]
                solutionSet = resultSet

        #Now since we have a set of solutions with the same number of meetings, find the one with the highest average
        #member attendance, also since everything is divided at the end by the same number im just not
        finalSolution = []
        bestAverage = 0
        for solution in solutionSet:
            averageMembers = 0
            for timeChunk in solution:
                averageMembers = averageMembers + len(timeChunk.members)
            if averageMembers > bestAverage:
                bestAverage = averageMembers
                finalSolution = solution

        return finalSolution

    def saveToFile(self, fileName):
        saveFile = open(fileName, "w")
        saveFile.write(str(self.times.size / self.times[0].size) + ", " + str(self.times[0].size)
                       + "," + str(len(self.members)) + ",\n")
        for member in self.members:
            member.save()
            saveFile.write(member.name + ",")
        saveFile.write("\n")
        for day in self.times:
            dayLine = ""
            for time in day:
                dayLine = dayLine + str(time) + ","
            saveFile.write(dayLine + "\n")

        saveFile.close()

    def loadFromFile(self, fileName):
        loadFile = open(fileName, "r")
        metaData = loadFile.readline().split(",")
        days = metaData[0]
        times = metaData[1]
        numMembers = int(metaData[2])
        memberNames = loadFile.readline().split(",")
        for member in range(numMembers):
            user = User.User("", "")
            user.load(memberNames[member])
            self.members.append(user)
        self.calculateTimes()

def findMeetingTime(chunks, membersRemaining, layersRemaining):
    thisChunk = chunks.pop(0)

    layersRemaining = layersRemaining - 1;
    for chunkMember in thisChunk.members:
        try:
            membersRemaining.remove(chunkMember)
        except:
            i =0# another throwaway

    if layersRemaining <= 0:
        if membersRemaining == []:
            return [[thisChunk]]
        else:
            return []

    solutionList = []
    for i in range(len(chunks) - layersRemaining + 1):
        resultList = findMeetingTime(chunks.copy(), membersRemaining.copy(), layersRemaining)
        if resultList != []:
            for result in resultList:
                result.insert(0, thisChunk)
                solutionList.append(result)
        del chunks[0]
    return solutionList
