from django.urls import path
from .views import *

urlpatterns = [

    path('tasks/',TasksList.as_view(),name="tasks_list"),
    path('tasks/create',CreateTask.as_view(),name="tasks_create"),
    path('tasks/edit/<int:pk>',UpdateTask.as_view(),name="tasks_edit"),
    path('tasks/delete/<int:pk>',DeleteTask.as_view(),name="tasks_delete"),
    path('tasks/done/<int:pk>',DoneTask.as_view(),name="tasks_done"),
    
   
]