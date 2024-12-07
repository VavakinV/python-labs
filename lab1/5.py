import re

def find_dates(text):
    date_pattern = r'\b(0?[1-9]|[12][0-9]|3[01])\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+(\d{4})?\b'
    
    dates = re.findall(date_pattern, text)
    
    return [' '.join(date) for date in dates]

s = input("Введите строку: ")
print(find_dates(s))

