from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskView.as_view(), name='task'),
    path('<int:id>/', views.TaskDetailView.as_view(), name='task_detail'),
]
