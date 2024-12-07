n = int(input())
results = {}
for i in range(n):
    inp =  input().split()
    candidate, votes = inp[0], int(inp[1])
    if candidate in results.keys():
        results[candidate] += votes
    else:
        results[candidate] = votes
print()
for item in sorted(results.items(), key=lambda x: x[0]):
    print(item[0], item[1])