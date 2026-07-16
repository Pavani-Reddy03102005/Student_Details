from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add-student/', views.add_student, name='add-student'),
    path("details/<int:id>/", views.details, name='details'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete-student'),
    path('api/students/', views.StudentListCreateAPI.as_view(), name='Student-List-Create'),
    path('api/students/<int:id>/', views.StudentListCreateAPI.as_view(), name='Student-Retrieve-Update-Destroy'),
]