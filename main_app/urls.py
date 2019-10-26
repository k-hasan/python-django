from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),

]