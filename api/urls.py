from django.urls import path
from .views import apiOverview, taskList, taskCreate, taskDetail, taskDelete, taskUpdate

urlpatterns = [
    path('',apiOverview.as_view(), name='api-overview'),
    path('task-list/',taskList.as_view(), name='task-list'),
    path('task-detail/<int:pk>/', taskDetail.as_view(), name = 'task-detail'),
    path('task-create/',taskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', taskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', taskDelete.as_view(), name = 'task-delete'),

]
