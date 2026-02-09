from django.urls import path
from . import views

urlpatterns = [
    path('', views.scheduler_list, name='scheduler_list'),
    path('create/', views.scheduler_create, name='scheduler_create'),  
    path('edit/<int:pk>/', views.scheduler_edit, name='scheduler_edit'),
    path('delete/<int:pk>/', views.scheduler_delete, name='scheduler_delete'),
]
