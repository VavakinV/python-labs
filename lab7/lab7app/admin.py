from django.contrib import admin
from .models import Vehicle, Driver, VehicleAssignment

# Регистрация модели Vehicle в админке
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'type', 'model', 'brand', 'manufacture_year', 'registration_number')  # Список отображаемых полей
    search_fields = ('type', 'model', 'brand', 'registration_number')  # Поля для поиска
    list_filter = ('type', 'brand')  # Фильтры по полям

# Регистрация модели Driver в админке
class DriverAdmin(admin.ModelAdmin):
    list_display = ('driver_id', 'first_name', 'last_name', 'license_number', 'birth_date', 'driving_experience')
    search_fields = ('first_name', 'last_name', 'license_number')  # Поля для поиска
    list_filter = ('birth_date', 'driving_experience')  # Фильтры по полям

# Регистрация модели VehicleAssignment в админке
class VehicleAssignmentAdmin(admin.ModelAdmin):
    list_display = ('assignment_id', 'vehicle', 'driver', 'assignment_date', 'return_date')
    search_fields = ('vehicle__registration_number', 'driver__license_number')  # Поля для поиска (через связь)
    list_filter = ('assignment_date', 'return_date')  # Фильтры по полям

# Регистрация моделей
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(VehicleAssignment, VehicleAssignmentAdmin)
