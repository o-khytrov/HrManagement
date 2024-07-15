from django.shortcuts import render
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import Employee


class EmployeeListJson(BaseDatatableView):
    # Define the model you're querying from
    model = Employee

    # Define columns that you want to include
    columns = ['first_name', 'last_name', 'email', 'department', 'hire_date']

    # Define searchable columns
    searchable_columns = ['first_name', 'last_name', 'email', 'department']

    # Define orderable columns
    order_columns = ['first_name', 'last_name', 'email', 'department', 'hire_date']


def hierarchy_view(request):
    top_managers = Employee.objects.filter(manager__isnull=True)
    return render(request, 'employee_hierarchy.html', {'top_managers': top_managers})


def load_subordinates(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    subordinates = employee.subordinates.all().select_related('manager')
    return render(request, 'employee_node.html', {'employees': subordinates})


def employee_list(request):
    return render(request, 'employee_list.html')
