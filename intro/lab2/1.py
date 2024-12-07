n = int(input("Введите число (не меньше 2): "))

divisor = 2
while n % divisor != 0:
    divisor += 1


print("Наименьший делитель:", divisor)