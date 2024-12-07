# 1
MKAD_LEN = 109
v = int(input("Введите скорость v: "))
t = int(input("Введите время t: "))

print(f"Вася на {str(v*t%MKAD_LEN)} км МКАДА")