from django.urls import path
from .views import TaskListCreateView, TaskDetailView, ImportantTaskListView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path("tasks/important/", ImportantTaskListView.as_view(), name="important-tasks"),
]
