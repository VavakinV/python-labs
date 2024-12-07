print("Введите последовательность:")
n = -1
max_n = -1
i = -1
max_i = 0
while n != 0:
    n = int(input())
    i += 1
    if n > max_n:
        max_n = n
        max_i = i

print(f"Индекс наибольшего элемента (начиная с 0): {max_i}")