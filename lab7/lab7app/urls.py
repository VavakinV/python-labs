from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('drivers/', views.drivers, name='drivers'),
    path('assignments/', views.assignments, name='assignments'),
    path('drivers/add/', views.add_driver, name='add_driver'),
    path('drivers/detail/<int:driver_id>/', views.driver_detail, name='driver_detail'),
    path('drivers/edit/<int:driver_id>/', views.edit_driver, name='edit_driver'),
    path('drivers/delete/<int:driver_id>/', views.delete_driver, name='delete_driver'),
    path('vehicles/add/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/detail/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicles/edit/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicles/delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('assignments/add/', views.add_assignment, name='add_assignment'),
    path('assignments/detail/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('assignments/edit/<int:assignment_id>/', views.edit_assignment, name='edit_assignment'),
    path('assignments/delete/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
]
