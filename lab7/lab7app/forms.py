from django import forms
from .models import Driver, Vehicle, VehicleAssignment

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'license_number', 'birth_date', 'driving_experience']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['type', 'model', 'brand', 'manufacture_year', 'registration_number']


class VehicleAssignmentForm(forms.ModelForm):
    class Meta:
        model = VehicleAssignment
        fields = ['vehicle', 'driver', 'assigned_date']

    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=True, label="Транспортное средство")
    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), required=True, label="Водитель")
    assigned_date = forms.DateField(widget=forms.SelectDateWidget(), required=True, label="Дата назначения")

