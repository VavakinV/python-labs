#!/usr/bin/env python

import sqlite3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
vehicle_id = form.getvalue("vehicle_id")
driver_id = form.getvalue("driver_id")
assign_date = form.getvalue("assign_date")
return_date = form.getvalue("return_date")

connection = sqlite3.connect("../transport.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO VehicleAssignments (VehicleID, DriverID, AssignmentDate, ReturnDate)
VALUES (?, ?, ?, ?)
""", (vehicle_id, driver_id, assign_date, return_date))

connection.commit()
connection.close()

print("Content-Type: text/html\n")
print("<html><body>")
print("<h1>Транспорт назначен водителю</h1>")
print(f"<p>ID транспортного средства: {vehicle_id}</p>")
print(f"<p>ID водителя: {driver_id}</p>")
print(f"<p>Дата назначения: {assign_date}</p>")
if return_date:
    print(f"<p>Дата возврата: {return_date}</p>")
else:
    print("<p>Дата возврата: отсутствует</p>")
print('<a href="/index.html"><button>Назад</button></a>')
print("</body></html>")