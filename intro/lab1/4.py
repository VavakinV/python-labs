def Cx2(x):
    return sum(range(1, x))


n = int(input("Введите n: "))
m = int(input("Введите m: "))


print(f"Максимум рукопожатий: {Cx2(n-(m-1))}")
team_value = n//m+(n%m!=0)
teams = m-(n%m!=0)
print(f"Минимум рукопожатий: {((team_value - (n%m == 1)) != 1) * Cx2(team_value)*teams}")

# Cx2(team_value)*teams+Cx2(n-team_value*teams)