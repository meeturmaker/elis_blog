from django.urls import path

from . import views

urlpatterns = [
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('health', views.health, name='health'),
    path('management', views.management, name='management'),
    path('travel', views.travel, name='travel'),
    path('fashion', views.fashion, name='fashion'),
    path('family', views.family, name='family'),
    
]
