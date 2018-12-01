"""
    name: Michelle Cortez
    Date: 11/27/2019
    Purpose: In class how to read from a txt file


"""

readFile = open("courses.txt", "r")
lines = readFile.readlines()
# print(len(lines))

aryCourses = []

for line in lines:
    # print(line)
    line = line.strip()
    # print(line)
    aryTemp = line.split(",")
    # print(aryTemp)
    aryCourses.append(aryTemp)
print(aryCourses)
readFile.close()