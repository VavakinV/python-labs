n = int(input("Введите N: "))
m = int(input("Введите M: "))
x = int(input("Введите x: "))
y = int(input("Введите y: "))

long_edge = max(n, m)
short_edge = min(n,m)

print(f"Необходимо проплыть минимум {min(x, long_edge-x, y, short_edge-y)}м")