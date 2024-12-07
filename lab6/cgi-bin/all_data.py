#!/usr/bin/env python

import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("../transport.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM Vehicles")
vehicles = cursor.fetchall()

cursor.execute("SELECT * FROM Drivers")
drivers = cursor.fetchall()

cursor.execute("SELECT * FROM VehicleAssignments")
assignments = cursor.fetchall()

connection.close()

print("Content-Type: text/html\n")
print("<html><body>")
print("<h1>Полная информация о данных в базе</h1>")

print("<h2>Транспортные средства</h2>")
print("<table border='1'>")
print("<tr><th>ID</th><th>Тип</th><th>Модель</th><th>Марка</th><th>Год выпуска</th><th>Рег. номер</th></tr>")
for vehicle in vehicles:
    print(f"<tr><td>{vehicle[0]}</td><td>{vehicle[1]}</td><td>{vehicle[2]}</td><td>{vehicle[3]}</td><td>{vehicle[4]}</td><td>{vehicle[5]}</td></tr>")
print("</table>")

print("<h2>Водители</h2>")
print("<table border='1'>")
print("<tr><th>ID</th><th>Имя</th><th>Фамилия</th><th>Номер водительского удостоверения</th><th>Дата рождения</th><th>Водительский стаж (лет)</th></tr>")
for driver in drivers:
    print(f"<tr><td>{driver[0]}</td><td>{driver[1]}</td><td>{driver[2]}</td><td>{driver[3]}</td><td>{driver[4]}</td><td>{driver[5]}</td></tr>")
print("</table>")

print("<h2>Назначения транспортных средств</h2>")
print("<table border='1'>")
print("<tr><th>ID</th><th>Транспортное средство</th><th>Водитель</th><th>Дата назначения</th><th>Дата возврата</th></tr>")
for assignment in assignments:
    print(f"<tr><td>{assignment[0]}</td><td>{assignment[1]}</td><td>{assignment[2]}</td><td>{assignment[3]}</td><td>{assignment[4]}</td></tr>")
print("</table>")

print('<br><br><a href="/index.html"><button>Вернуться на главную</button></a>')

print("</body></html>")