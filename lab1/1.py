import math


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n%i == 0:
            return False

    return True


def max_prime_divisor(n):
    result = "Нет простых делителей"
    for i in range(2, n+1):
        if is_prime(i) and n%i == 0:
            result = i
    return result


def digits_mult(n):
    result = 1

    while n >= 1:
        last_digit = n % 10
        result *= last_digit
        n //= 10

    return result


def not5_digits_mult(n):
    result = 1

    while n >= 1:
        last_digit = n % 10
        if last_digit % 5 != 0:
            result *= last_digit
        n //= 10
    return result


def max_odd_not_prime_divisor(n):
    result = 1

    for i in range(2, n+1):
        if (n % i == 0) and not (is_prime(i)) and (i % 2 == 1):
            result = i

    return result


def div_mult_gcd(n):
    monpd = max_odd_not_prime_divisor(n)
    dm = digits_mult(n)

    result = 1
    for i in range(1, max(monpd, dm)):
        if monpd%i == 0 and dm%i == 0:
            result = i

    return result


n = int(input("Введите число n: "))
print(f"Максимальный простой делитель: {max_prime_divisor(n)}")
print(f"Произведение цифр, не делящихся на 5: {not5_digits_mult(n)}")
print(f"НОД максимального нечетного непростого делителя и произведения цифр: {div_mult_gcd(n)}")