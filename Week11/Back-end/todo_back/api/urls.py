from django.urls import path
from api import views

urlpatterns=[
    path('',views.index),
    path('task_lists/',views.tasklists),
    path('task_lists/<int:pk>/', views.task_detail),
    path('task_lists/<int:pk>/tasks', views.tasks),
]
© 2019 GitHub, Inc.