from django.urls import path
from ur_auth import views


app_name = 'ur-auth'

urlpatterns = [
    path('', views.home, name='home'),
]
