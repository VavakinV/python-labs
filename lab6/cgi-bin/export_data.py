#!/usr/bin/env python

import sqlite3
import json
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

data = {
    "vehicles": [
        {"id": vehicle[0], "type": vehicle[1], "model": vehicle[2], "brand": vehicle[3], "year": vehicle[4], "reg_number": vehicle[5]}
        for vehicle in vehicles
    ],
    "drivers": [
        {"id": driver[0], "first_name": driver[1], "last_name": driver[2], "license_number": driver[3], "birth_date": driver[4], "experience": driver[5]}
        for driver in drivers
    ],
    "assignments": [
        {"id": assignment[0], "vehicle_id": assignment[1], "driver_id": assignment[2], "assign_date": assignment[3], "return_date": assignment[4]}
        for assignment in assignments
    ]
}

with open("transport_data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Content-Type: text/html\n")
print("<html><body>")
print("<h1>Данные экспортированы в JSON файл</h1>")
print('<a href="/index.html"><button>Назад</button></a>')
print("</body></html>")