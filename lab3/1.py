def max_product(N, K, readings):
    max1 = [0] * N 
    max2 = [0] * N
    max3 = 0

    for i in range(N):
        max1[i] = max(readings[i], max1[i-1]) if i > 0 else readings[i]

    for i in range(N):
        if i >= K:
            max2[i] = max(max2[i-1], max1[i-K] * readings[i])
        else:
            max2[i] = max2[i-1]

    for i in range(N):
        if i >= 2 * K:
            max3 = max(max3, max2[i-K] * readings[i])
    
    return max3 % (10**6 + 1)

def process_file(filename):
    with open(filename) as f:
        first_line = f.readline().strip()
        N, K = map(int, first_line.split())
        readings = [int(f.readline().strip()) for _ in range(N)]
    
    return max_product(N, K, readings)

result_a = process_file('lab3/27-168a.txt')
result_b = process_file('lab3/27-168b.txt')

# print(max_product(6, 2, [15, 14, 20, 23, 21, 10]))
print(result_a, result_b)

