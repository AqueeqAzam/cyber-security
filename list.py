# opertaion on list
portList = [21, 22, 80, 6668, 3000]
print(portList[0])

serverError = [401, 404, 500]
print("Internal server error:", serverError[2])

# append method
portList.append(443)
print(portList)

# delete method
portList.remove(80)
print(portList)

# insert method
portList.insert(1,80)
print(portList)

# sorting method
portList.sort()
print(portList)

# length method
portList.len()
print(portList)

# application in scanning
scn = portList.index(80)
print("There is " + str(scn) + " port to scan before 80")
