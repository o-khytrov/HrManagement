from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee


def index(request):
    employees = Employee.objects.all()
    hierarchy = build_hierarchy(employees)
    return render(request, 'employee_hierarchy.html', {'hierarchy': hierarchy})


def build_hierarchy(employees):
    employee_dict = {employee.id: employee for employee in employees}
    hierarchy = []

    for employee in employees:
        if employee.manager_id is None:
            hierarchy.append(employee)
        else:
            manager = employee_dict[employee.manager_id]
            if not hasattr(manager, 'subordinate_list'):
                manager.subordinate_list = []
            manager.subordinate_list.append(employee)

    return hierarchy
