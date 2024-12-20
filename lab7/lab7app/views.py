from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Vehicle, Driver, VehicleAssignment
from .forms import DriverForm, VehicleForm, VehicleAssignmentForm

# Главная страница
def home(request):
    return render(request, 'home.html')

# Страница с таблицей транспортных средств
def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})

# Страница с таблицей водителей
def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers.html', {'drivers': drivers})

# Страница с таблицей назначений транспортных средств
def assignments(request):
    assignments = VehicleAssignment.objects.all()
    return render(request, 'assignments.html', {'assignments': assignments})

# Страница добавления нового водителя
def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drivers')  # После добавления водителя перенаправляем обратно на страницу с водителями
    else:
        form = DriverForm()
    
    return render(request, 'add_driver.html', {'form': form})

# Представление для страницы с подробной информацией
def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, driver_id=driver_id)
    return render(request, 'driver_detail.html', {'driver': driver})

# Представление для редактирования водителя
def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('drivers')  # Перенаправление после успешного обновления
    else:
        form = DriverForm(instance=driver)

    return render(request, 'edit_driver.html', {'form': form, 'driver': driver})

# Представление для удаления водителя
def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    
    if request.method == 'POST':
        driver.delete()
        return redirect('drivers')  # Перенаправление после удаления записи

    return render(request, 'delete_driver_confirmation.html', {'driver': driver})


# Страница добавления нового транспортного средства
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles')  # После добавления транспортного средства перенаправляем на страницу со списком транспортных средств
    else:
        form = VehicleForm()

    return render(request, 'add_vehicle.html', {'form': form})


# Представление для страницы с подробной информацией о транспортном средстве
def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, vehicle_id=vehicle_id)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})


# Представление для редактирования транспортного средства
def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicles')  # Перенаправление после успешного обновления
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'edit_vehicle.html', {'form': form, 'vehicle': vehicle})


# Представление для удаления транспортного средства
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicles')  # Перенаправление после удаления записи

    return render(request, 'delete_vehicle_confirmation.html', {'vehicle': vehicle})

# Страница добавления нового задания
def add_assignment(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle')
        driver_id = request.POST.get('driver')
        assignment_date = request.POST.get('assignment_date')

        vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
        driver = Driver.objects.get(driver_id=driver_id)

        # Создаем новое задание
        new_assignment = VehicleAssignment(
            vehicle=vehicle,
            driver=driver,
            assignment_date=assignment_date
        )
        new_assignment.save()
        return redirect('assignments')  # Перенаправление после добавления задания

    else:
        vehicles = Vehicle.objects.all()  # Получаем все транспортные средства
        drivers = Driver.objects.all()  # Получаем всех водителей

    return render(request, 'add_assignment.html', {'vehicles': vehicles, 'drivers': drivers})


# Страница с подробной информацией о назначении
def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(VehicleAssignment, assignment_id=assignment_id)
    return render(request, 'assignment_detail.html', {'assignment': assignment})


def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(VehicleAssignment, assignment_id=assignment_id)

    if request.method == 'POST':
        # Получаем данные из формы
        vehicle_id = request.POST.get('vehicle_id')
        driver_id = request.POST.get('driver_id')
        assignment_date = request.POST.get('assignment_date')
        return_date = request.POST.get('return_date')

        # Обновляем данные назначения
        assignment.vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
        assignment.driver = get_object_or_404(Driver, pk=driver_id)
        assignment.assignment_date = assignment_date
        assignment.return_date = return_date if return_date else None
        assignment.save()

        # Перенаправляем на страницу списка назначений
        return redirect('assignments')

    # Отображаем форму
    return render(request, 'edit_assignment.html', {
        'assignment': assignment,
    })



# Страница подтверждения удаления назначения
def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(VehicleAssignment, pk=assignment_id)
    
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignments')  # Перенаправление после удаления назначения

    return render(request, 'delete_assignment_confirmation.html', {'assignment': assignment})
