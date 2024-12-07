strings = []
s = input("Введите строки: ")
while s != "":
    strings.append(s)
    s = input()

print(f"Отсортированные по длине строки: {sorted(strings, key=len)}")