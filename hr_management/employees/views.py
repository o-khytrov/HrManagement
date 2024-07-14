# employees/views.py
from django.http import JsonResponse
from django.shortcuts import render

from .models import Employee


def hierarchy_view(request):
    top_managers = Employee.objects.filter(manager__isnull=True)
    return render(request, 'employee_hierarchy.html', {'top_managers': top_managers})


def load_subordinates(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    subordinates = employee.subordinates.all().select_related('manager')
    data = [
        {
            'id': sub.id,
            'full_name': sub.full_name,
            'position': sub.position,
            'has_subordinates': sub.subordinates.exists()
        }
        for sub in subordinates
    ]
    return JsonResponse(data, safe=False)


def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})
