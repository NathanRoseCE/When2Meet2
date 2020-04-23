# User class is only used for testing
# import User

class TimeChunk:
    def __init__(self, startTime, endTime, members):
        self.startTime = startTime
        self.endTime = endTime
        self.members = members

    def toString(self):
        string = ""
        string = str(self.startTime) + " " + str(self.endTime) + " "
        for member in self.members:
            string = string + member.name  + " "
        return string

def determineAllChunks(members):
    allChunks = []
    if members == []:
        allChunks.append(TimeChunk([0, 0], [7, 48], 0))
        return allChunks

    numDays = int(members[0].times.size / members[0].times[0].size)
    numTimes = members[0].times[0].size
    allChunks.append(TimeChunk([0, 0], [numDays-1, numTimes-1], membersAtTime(0, 0, members)))

    # For each time segment
    for day in range(numDays):
        for time in range(numTimes):
            # If the members in this time are different then the current time chunk, change the chunk
            nowsMembers = membersAtTime(day, time, members)
            if allChunks[-1].members != nowsMembers:
                if time == 0:
                    allChunks[-1].endTime = [day-1, numTimes-1]
                else:
                    allChunks[-1].endTime = [day, time-1]

                allChunks.append(TimeChunk([day,time], [numDays-1, numTimes-1], nowsMembers))
            # If not just keep checking
    return allChunks

def membersAtTime(day, time, members):
    membersAvailable = [];
    for member in members:
        if member.times[day][time] != 0:
            membersAvailable.append(member)
    return membersAvailable




# test software for Time Chunks
# userOne = User.User("gfdagreasgres", "Nathan")
# userOne.changeAvailibility(0, 0)
# userOne.changeAvailibility(1, 2)
# userOne.changeAvailibility(1, 3)
# userTwo = User.User("fhregbieragboahg", "Abby")
# userTwo.changeAvailibility(1, 1)
# userTwo.changeAvailibility(1, 2)
# userTwo.changeAvailibility(1, 3)
#
# testChunks = determineAllChunks([userOne, userTwo])
# for chunk in testChunks:
#     print(chunk.toString())