from django.urls import path

from . import views
from .views import EmployeeListJson

urlpatterns = [
    path('hierarchy/', views.hierarchy_view, name='hierarchy'),
    path('list/', views.employee_list, name='employee_list.html'),
    path('employee_list_data/', EmployeeListJson.as_view(), name='employee_list_json'),
    path('load_subordinates/<int:employee_id>/', views.load_subordinates, name='load_subordinates'),

    path('create/', views.employee_create_view, name='employee_create'),
    path('update/<int:pk>/', views.employee_update_view, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete_view, name='employee_delete'),
    path('employee_autocomplete/', views.employee_autocomplete, name='employee_autocomplete'),
]
