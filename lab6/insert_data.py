import sqlite3

connection = sqlite3.connect('transport.db')
cursor = connection.cursor()

vehicles_data = [
    ("Автомобиль", "Camry", "Toyota", 2020, "А123ВС77"),
    ("Автобус", "Sprinter", "Mercedes-Benz", 2018, "М456ОР99"),
    ("Мотоцикл", "CBR600RR", "Honda", 2022, "К789ЕХ77")
]

cursor.executemany('''
INSERT INTO Vehicles (Type, Model, Brand, ManufactureYear, RegistrationNumber)
VALUES (?, ?, ?, ?, ?)
''', vehicles_data)

drivers_data = [
    ("Иван", "Петров", "77ВУ123456", "1985-05-20", 15),
    ("Алексей", "Сидоров", "99АР789012", "1990-11-15", 10),
    ("Ольга", "Иванова", "50СР345678", "1995-03-10", 7)
]

cursor.executemany('''
INSERT INTO Drivers (FirstName, LastName, LicenseNumber, BirthDate, DrivingExperience)
VALUES (?, ?, ?, ?, ?)
''', drivers_data)

assignments_data = [
    (1, 1, "2024-12-01", "2024-12-05"),
    (2, 2, "2024-12-02", None),
    (3, 3, "2024-12-03", "2024-12-04")
]

cursor.executemany('''
INSERT INTO VehicleAssignments (VehicleID, DriverID, AssignmentDate, ReturnDate)
VALUES (?, ?, ?, ?)
''', assignments_data)

connection.commit()
connection.close()
