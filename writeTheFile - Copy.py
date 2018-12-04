aryCourses = [['CIS130', '3', 'Spring'],['CIS150','3','Spring'],['MTH110','4','Spring'],['CIS131', '4','Javascript']]

write_file = open("out.txt", "w")
# write_file.write("I love puppies")

for course in aryCourses:
    # print(course)
    courseLine = f"{course[0]},{course[1]},{course[2]}\n"
    print(courseLine)
    write_file.write(courseLine)
write_file.close()