print("Комарницький Нестор \nГрупа КНМС-11 \nЗнаходження найбільшого числа з трьох(4 лабораторна робота)")

a = int(input("Введіть 1 число: "))
b = int(input("Введіть 2 число: "))
c = int(input("Введіть 3 число: "))

if a > b and a > c:
	max = ("перше", a)
elif b > a and b > c:
	max = ("друге", b)
elif c > b and c > a:
	max = ("третє", c)
else:
	print("Числа мають бути різними!")
	exit()

print(f"Найбільшим числом є {max[0]} - {max[1]}") 

