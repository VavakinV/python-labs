class1 = int(input("Введите кол-во учащихся в первом классе: "))
class2 = int(input("Введите кол-во учащихся во втором классе: "))
class3 = int(input("Введите кол-во учащихся в третьем классе: "))

print(f"Нужно минимум {class1//2 + class2//2 + class3//2 + class1%2 + class2%2 +class3%2} парт")