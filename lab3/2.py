import random

def generate_random_numbers(filename, N, lower_bound=-100, upper_bound=100):
    with open(filename, 'w') as f:
        for _ in range(N):
            number = random.randint(lower_bound, upper_bound)
            f.write(f"{number}\n")

def count_opposite_pairs(filename):
    with open(filename) as f:
        numbers = [int(line.strip()) for line in f]

    unique_numbers = set(numbers)
    count = 0
    
    for num in unique_numbers:
        if -num in unique_numbers:
            count += 1

    return count

N = 100
filename = 'lab3/random_numbers.txt'

generate_random_numbers(filename, N)

opposite_pairs_count = count_opposite_pairs(filename)

print(f"Количество пар противоположных чисел: {opposite_pairs_count}")
