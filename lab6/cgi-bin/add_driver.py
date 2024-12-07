#!/usr/bin/env python

import sqlite3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
first_name = form.getvalue("first_name")
last_name = form.getvalue("last_name")
license_number = form.getvalue("license_number")
birth_date = form.getvalue("birth_date")
experience = form.getvalue("experience")

connection = sqlite3.connect("../transport.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO Drivers (FirstName, LastName, LicenseNumber, BirthDate, DrivingExperience)
VALUES (?, ?, ?, ?, ?)
""", (first_name, last_name, license_number, birth_date, experience))

connection.commit()
connection.close()

print("Content-Type: text/html\n")
print("<html><body>")
print("<h1>Водитель добавлен</h1>")
print(f"<p>Имя: {first_name}</p>")
print(f"<p>Фамилия: {last_name}</p>")
print(f"<p>Номер удостоверения: {license_number}</p>")
print(f"<p>Дата рождения: {birth_date}</p>")
print(f"<p>Стаж: {experience} (лет)</p>")
print('<a href="/index.html"><button>Назад</button></a>')
print("</body></html>")