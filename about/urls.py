from .import views
from django.urls import path
urlpatterns = [
   path('about_section/', views.about_section, name='about_section'),
]