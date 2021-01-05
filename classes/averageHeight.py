student_heights = input("Input a list of student heights ").split()


for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


totalHeight = 0
for height in student_heights:
    totalHeight += height

    
numOfStudents = 0
for student in student_heights:
    numOfStudents += 1


average = round(totalHeight / numOfStudents)
print(average)