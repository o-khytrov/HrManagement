from django.shortcuts import render

from .models import Employee


def hierarchy_view(request):
    top_managers = Employee.objects.filter(manager__isnull=True)
    return render(request, 'employee_hierarchy.html', {'top_managers': top_managers})


def load_subordinates(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    subordinates = employee.subordinates.all().select_related('manager')
    return render(request, 'employee_node.html', {'employees': subordinates})


def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})
