from django.urls import path
from api import views

app_name='api'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name ='list'),
    path("register", views.registration_view, name='register'),
    path('login', views.login_view, name='login'),
    path('add-task', views.add_tasks_to_account, name='add-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),

]
