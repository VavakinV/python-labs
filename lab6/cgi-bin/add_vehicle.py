#!/usr/bin/env python

import sqlite3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
type_ = form.getvalue("type")
model = form.getvalue("model")
brand = form.getvalue("brand")
year = form.getvalue("year")
reg_number = form.getvalue("reg_number")

connection = sqlite3.connect("../transport.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO Vehicles (Type, Model, Brand, ManufactureYear, RegistrationNumber)
VALUES (?, ?, ?, ?, ?)
""", (type_, model, brand, year, reg_number))

connection.commit()
connection.close()

print("Content-Type: text/html\n")
print("<html><body>")
print("<h1>Транспортное средство добавлено</h1>")
print(f"<p>Тип: {type_}</p>")
print(f"<p>Модель: {model}</p>")
print(f"<p>Марка: {brand}</p>")
print(f"<p>Год выпуска: {year}</p>")
print(f"<p>Регистрационный номер: {reg_number}</p>")
print('<a href="/index.html"><button>Назад</button></a>')
print("</body></html>")