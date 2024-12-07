import math

M = int(input("Введите количество этажей M: "))
K1 = int(input("Введите искомую квартиру K1: "))
K2 = int(input("Введите известную квартиру K2: "))
P2 = int(input("Введите подъезд известной квартиры P2: "))
N2 = int(input("Введите этаж известной квартиры N2: "))

apartments_per_floor = (K2 - 1) // ((P2 - 1) * M + (N2 - 1)) + 1

apartments_per_entrance = apartments_per_floor * M

P1 = math.ceil(K1 / apartments_per_entrance)

N1 = math.ceil((K1 - (apartments_per_entrance * (P1 - 1))) / apartments_per_floor)
print(f'Квартира {K1} находится в подъезде {P1}, на этаже {N1}.')
