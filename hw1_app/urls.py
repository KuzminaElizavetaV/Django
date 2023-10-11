from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('about/', views.AboutView.as_view(), name='about')
]
