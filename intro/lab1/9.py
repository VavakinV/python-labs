n = int(input("Введите количество кусков: "))
print(f"Разрезов необходимо сделать: {(n%2==0)*(n//2) + (n%2==1)*n}")