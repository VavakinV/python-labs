print("Введите последовательность:")
n = int(input())
first_max = n
n = int(input())
if n > first_max:
    first_max, second_max = n, first_max
else:
    second_max = n
while n != 0:
    n = int(input())
    if n > first_max:
        first_max, second_max = n, first_max
    elif first_max >= n > second_max:
        second_max = n
    else:
        pass

print(f"Второй по величине элемент последовательности: {second_max}")