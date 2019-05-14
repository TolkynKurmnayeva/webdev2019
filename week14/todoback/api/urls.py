from django.urls import path
from api import views


def func():
    pass


urlpatterns = [
    path('tasklists/', views.AllTaskLists.as_view()),
    path('tasklists/<int:pk>/', views.TaskListDetail.as_view()),
    path('tasklists/<int:pk>/tasks/', views.TLTasks.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
]