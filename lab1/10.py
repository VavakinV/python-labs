strings = []
s = input("Введите строки: ")
while s != "":
    strings.append(s)
    s = input()

print(f"Отсортированные по количеству слов: {sorted(strings, key=lambda x:len(x.split()))}")