from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('logout/', views.logout_view, name='logout')
]
