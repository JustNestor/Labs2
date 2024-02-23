print("Комарницький Нестор \nГрупа КНМС-11 \nЗнаходження найбільшого числа з поміж 3(6 лабораторна робота)")

def get_max(integers):
	return max(integers)

def get_input():
	try:
		integers = list(map(int, input("Введіть три числа через пробіл: ").split()))
	except:
		print("Введено не правильні дані!")
		exit()
		
	return integers

def give_output(mx):
	print(f"Максимальним числом є: {mx}")

def main():
	integers = get_input()
	mx = get_max(integers)
	give_output(mx)


main()