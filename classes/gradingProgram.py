student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


std_grades = {}

for student in student_scores:
	score = student_scores[student]
	if score > 90:
		std_grades[student] = "Outstanding"
	elif score > 80:
		std_grades[student] = "Exceeds expectations"
	elif score > 70:
		std_grades[student] = "acceptable"		
	else:
		std_grades[student] = "failed"	




print(std_grades)