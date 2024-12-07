n = int(input("Введите число n: "))

factorial = 1
total_sum = 0

for i in range(1, n + 1):
    factorial *= i
    total_sum += factorial


print(f"Сумма факториалов от 1 до {n}: {total_sum}")
