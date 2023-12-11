from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blogs/', views.blogs, name="blogs"),
    path('team/', views.team, name="team"),
    path('experience/', views.experience, name="experience"),
    path('travel/', views.travel, name="travel")

]
