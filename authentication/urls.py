from .views import login_user, register
from django.urls import path


urlpatterns = [
    path('', login_user, name='login'),
    path('register', register, name='register'),
]