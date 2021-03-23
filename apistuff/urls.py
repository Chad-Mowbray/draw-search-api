from django.urls import path
from .views import Process

urlpatterns = [
    path('', Process.as_view(), name='process')
]