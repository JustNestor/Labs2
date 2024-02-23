print("Комарницький Нестор \nГрупа КНМС-11 \nЗнаходження найбільшого та найменшого в двохвимірному масиві(7 лабораторна робота)")

amount_of_arrays = int(input("Введіть кількість масивів в двовимірному масиві: "))

elements_length = int(input("Введіть кількість елементів в масивах: "))

twod_array = []

for i in range(elements_length):
	try:
		array_tmp = list(map(int, input(f"Введіть {elements_length} числа через пробіл: ").split()))
	except:
		print("Введено не правильні дані!")
		exit()

	twod_array.append(array_tmp)

array_of_max_elements = []
array_of_min_elements = []

for array in twod_array:
	array_of_max_elements.append(max(array))
	array_of_min_elements.append(min(array))

print(f"Максимальне значення: {max(array_of_max_elements)}")
print(f"Miнімальне: {min(array_of_min_elements)}")
