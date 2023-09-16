def sec_grade(students):
	grade = []
	for student in students:
		grade.append(student[1])

	grade = sorted(grade, reverse=True)
	print(grade)
	sec = grade[1]

	for student in students:
		if student[1] == sec:
			print(student[0])



def main():
	students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
	sec_grade(students)

main()