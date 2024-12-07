import re

def is_phone(string):
    pattern = r"^(?:\+7|8)\(?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$"
    return bool(re.match(pattern, string))

def is_phone_except(string):
    pattern = r"^(?:\+7|8)\(?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$"
    if not isinstance(string, str):
        raise ValueError("The argument must be a string.")
    if not re.match(pattern, string):
        raise ValueError(f"Invalid phone number format: {string}")
    return True

print("Функция 1:")
print(is_phone("+71234567890"))
print(is_phone("8(123)456-78-90"))
print(is_phone("+7(123)4567890"))
print(is_phone("1234567890"))
print(is_phone("xyz"))

print("\nФункция 2:")
print(is_phone_except("+71234567890"))  
print(is_phone_except("8(123)456-78-90"))
print(is_phone_except("+7(123)4567890"))
try:
    print(is_phone_except("1234567890"))
except ValueError as e:
    print(e)
try:
    print(is_phone_except(123))
except ValueError as e:
    print(e)