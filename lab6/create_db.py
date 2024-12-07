import sqlite3

connection = sqlite3.connect('transport.db')

cursor = connection.cursor()

# Vehicles
cursor.execute('''
CREATE TABLE IF NOT EXISTS Vehicles (
    VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
    Type TEXT NOT NULL,
    Model TEXT NOT NULL,
    Brand TEXT NOT NULL,
    ManufactureYear INTEGER NOT NULL,
    RegistrationNumber TEXT NOT NULL UNIQUE
)
''')

# Drivers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Drivers (
    DriverID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    LicenseNumber TEXT NOT NULL UNIQUE,
    BirthDate DATE NOT NULL,
    DrivingExperience INTEGER NOT NULL
)
''')

# VehicleAssignments
cursor.execute('''
CREATE TABLE IF NOT EXISTS VehicleAssignments (
    AssignmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    VehicleID INTEGER NOT NULL,
    DriverID INTEGER NOT NULL,
    AssignmentDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
)
''')

connection.commit()
connection.close()
