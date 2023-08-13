from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('basses/', views.bass_index, name="bass_index"),
    path('basses/<int:bass_id>', views.bass_details, name="bass_details")
]