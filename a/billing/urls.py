from django.urls import path
from .views import index, index2, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('a/', index2, name='index2'),
    path('dashboard/', dashboard, name='dashboard'),
]
