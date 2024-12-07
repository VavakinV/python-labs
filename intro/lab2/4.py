print("Введите последовательность:")
n = int(input())
prev = n
max_streak = 0
curr_streak = 1
while n != 0:
    n = int(input())
    if n == prev:
        curr_streak += 1
    else:
        curr_streak = 1
    prev = n
    if curr_streak > max_streak:
        max_streak = curr_streak

print(f"Длина наибольшей цепочки повторяющихся чисел: {max_streak}")