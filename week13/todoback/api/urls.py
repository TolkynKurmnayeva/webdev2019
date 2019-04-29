from django.urls import path
from api import views

# urlpatterns = [
#     path('task_list/', views.task_list),
#     path('task_list/<int:pk>/', views.task_list_actions)
# ]

urlpatterns = [
    path('task_list/', views.AllTaskList.as_view()),
    path('task_list/<int:pk>/', views.TaskListDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)

]