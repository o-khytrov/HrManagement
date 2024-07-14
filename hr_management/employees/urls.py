from django.urls import path

from . import views

urlpatterns = [
    path('hierarchy/', views.hierarchy_view, name='hierarchy'),
    path('list/', views.employee_list_view, name='employee_list'),
    path('load_subordinates/<int:employee_id>/', views.load_subordinates, name='load_subordinates'),
]