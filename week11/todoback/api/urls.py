from django.urls import path, re_path

from api import views

urlpatterns = [
    path('task_list/', views.task_list),
    path('task_list/<int:pk>/tasks', views.task_detail),
    path('task_list/<int:pk>/', views.task_get)
]