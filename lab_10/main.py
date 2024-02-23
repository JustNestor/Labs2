from dataclasses import dataclass

print("Комарницький Нестор \nГрупа КНМС-11 \nСтуденти(10 лабораторна робота)")

@dataclass
class Student:
	second_name: str
	first_name: str
	patronymics: str 
	birth_year: int
	group: str
	rating: int
	male: str

students = []

for i in range(3):
	data = input("Прізвище Ім'я По-батькові Рік народження Група Рейтинг Стать: ").split()

	if len(data) != 7:
		print("Невірна кількість даних!")
		exit()
	if data[6].lower() != "чоловік" and data[6].lower() != "жінка":
		print("Невірна стать!")
		exit()

	student = Student(data[0], data[1], data[2], int(data[3]), data[4], int(data[5]), data[6].lower())

	students.append(student)

for student in students:
	if student.rating < 50:
		print(f"{student.first_name[0]}. {student.patronymics[0]}. {student.second_name}")
