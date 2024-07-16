from django import forms
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'date_of_hire', 'email', 'id']
        widgets = {
            'id': forms.TextInput(attrs={'required': False}),
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'position': forms.TextInput(attrs={'required': True}),
            'date_of_hire': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
        }


class EmployeeListJson(BaseDatatableView):
    model = Employee

    columns = ['id', 'first_name', 'last_name', 'email', 'position', 'date_of_hire']

    searchable_columns = ['first_name', 'last_name', 'email', 'position']

    order_columns = ['first_name', 'last_name', 'email', 'position', 'date_of_hire']


def hierarchy_view(request):
    top_managers = Employee.objects.filter(manager__isnull=True)
    return render(request, 'employee_hierarchy.html', {'top_managers': top_managers})


def load_subordinates(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    subordinates = employee.subordinates.all().select_related('manager')
    return render(request, 'employee_node.html', {'employees': subordinates})


def employee_list(request):
    return render(request, 'employee_list.html')


def employee_autocomplete(request):
    if 'query' in request.GET:
        query = request.GET.get('query')
        employees = Employee.objects.filter(last_name__icontains=query)[:10]
        suggestions = list(employees.values('id', 'first_name', 'last_name'))
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)


@login_required
def employee_create_view(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, 'employee_form.html', {'form': form})


@login_required
def employee_update_view(request, pk):
    employee = Employee.objects.get(pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, 'employee_form.html', {'form': form})


@login_required
def employee_delete_view(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return JsonResponse({})
