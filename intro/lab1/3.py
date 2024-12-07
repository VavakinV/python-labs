n = int(input("Введите n: "))
m = int(input("Введите m: "))

print(f"Дней потребуется машине: {m//n + (m%n!=0)}")