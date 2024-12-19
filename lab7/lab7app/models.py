from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    manufacture_year = models.IntegerField()
    registration_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.registration_number})"

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField()
    driving_experience = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VehicleAssignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    assignment_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Assignment {self.assignment_id}: {self.vehicle} -> {self.driver}"
