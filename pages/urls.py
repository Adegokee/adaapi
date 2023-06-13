from django.urls import path
from . import views

urlpatterns = [
    path('createtodo/', views.createtodo, name='createtodo'),
    path('alltodo/', views.alltodo, name='alltodo'),
    path('delete/<int:id>/', views.tododelete, name='delete'),
    path('edit/<int:id>/', views.edittodo, name='edit'),
    path('', views.index, name='index'),
]
