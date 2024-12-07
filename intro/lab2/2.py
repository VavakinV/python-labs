n = int(input("Введите натуральное N: "))

power = -1
curr_two = 1

while curr_two <= n:
    power += 1
    curr_two *= 2

print(f"Наибольшая степень двойки, не превосходящая {n}: {power}")