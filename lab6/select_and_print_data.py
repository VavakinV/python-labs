import sqlite3

connection = sqlite3.connect('transport.db')
cursor = connection.cursor()

def fetch_and_print(query, description="Результаты запроса"):
    print(description)
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(" | ".join(column_names))
    print("-" * 50)
    for row in rows:
        print(" | ".join(map(str, row)))
    print("\n")

main_query_vehicles = """
SELECT * FROM Vehicles
"""

main_query_drivers = """
SELECT * FROM Drivers
"""

main_query_assignments = """
SELECT * FROM VehicleAssignments
"""

query1 = """
SELECT * FROM Vehicles
WHERE Type = 'Автомобиль'
"""
description1 = "Все транспортные средства типа 'Автомобиль'"

query2 = """
SELECT FirstName, LastName, LicenseNumber, DrivingExperience
FROM Drivers
WHERE DrivingExperience > 10
"""
description2 = "Водители со стажем более 10 лет"

query3 = """
SELECT Drivers.FirstName, Drivers.LastName, Vehicles.Type, Vehicles.Model, VehicleAssignments.AssignmentDate, VehicleAssignments.ReturnDate
FROM VehicleAssignments
JOIN Drivers ON VehicleAssignments.DriverID = Drivers.DriverID
JOIN Vehicles ON VehicleAssignments.VehicleID = Vehicles.VehicleID
WHERE VehicleAssignments.ReturnDate IS NULL
"""
description3 = "Транспортные средства, которые сейчас в использовании (без даты возврата)"

print("Полная информация о таблицах:")
fetch_and_print(main_query_vehicles)
fetch_and_print(main_query_drivers)
fetch_and_print(main_query_assignments)
fetch_and_print(query1, description1)
fetch_and_print(query2, description2)
fetch_and_print(query3, description3)

connection.close()