print("Комарницький Нестор \nГрупа КНМС-11 \nВведення 5 чисел послідовності та дії над ними(5 лабораторна робота)")

arr = []

for i in range(1, 6):
	a = float(input(f"Введіть число №{i}: "))

	arr.append(a)

	print(f"Сума: {sum(arr)}, середнє арифметичне: {sum(arr)/len(arr)}")