import Schedule
import User

test = Schedule.Schedule("fdsrehreahrea", "Test Schedule")
userOne = User.User("gfdagreasgres", "Nathan")
userOne.changeAvailibility(0, 2)
userOne.changeAvailibility(0, 3)
userOne.changeAvailibility(0, 4)
userOne.changeAvailibility(0, 11)
userOne.changeAvailibility(0, 12)
userOne.changeAvailibility(0, 13)
userOne.changeAvailibility(0, 14)
userOne.changeAvailibility(0, 15)
userOne.changeAvailibility(0, 16)
userOne.changeAvailibility(1, 0)
userOne.changeAvailibility(1, 1)
userOne.changeAvailibility(1, 2)
userOne.changeAvailibility(1, 3)
userOne.changeAvailibility(1, 4)
userOne.changeAvailibility(1, 5)
userTwo = User.User("fhregbieragboahg", "Abby")
userTwo.changeAvailibility(0, 9)
userTwo.changeAvailibility(0, 10)
userTwo.changeAvailibility(0, 11)
userTwo.changeAvailibility(0, 12)
userThree = User.User("fhjewbOFEWBOBEW", "Jackie")
userThree.changeAvailibility(0, 3)
userThree.changeAvailibility(0, 4)
userThree.changeAvailibility(0, 5)
userThree.changeAvailibility(0, 6)
userFour = User.User("fdjsbfoiewnbgoap", "Corrie")
userFour.changeAvailibility(1, 0)
userFour.changeAvailibility(1, 1)
userFour.changeAvailibility(1, 2)
userFour.changeAvailibility(1, 3)
userFive = User.User("fnejwbfpewhpewhp", "Teja")
userFive.changeAvailibility(1, 2)
userFive.changeAvailibility(1, 3)
userFive.changeAvailibility(1, 4)
userFive.changeAvailibility(1, 5)


print("Schedule Test")
test.addMember(userOne, True);
test.addMember(userTwo, False);
test.addMember(userThree, False);
test.addMember(userFour, False);
test.addMember(userFive, False);

#test.calculateTimes();
#print(test.times)
#bestTimes = test.findBestTime()
#print(bestTimes)
#for time in bestTimes:
#    print(time)
#    members = test.membersAtTime(time)
#    for member in members:
#        print(member.name)
#    print()


print("Algorithm SOlution")
print()
solution = test.determineBestMeetingTime()
for time in solution:
    print(time.toString())
