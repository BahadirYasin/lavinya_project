from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservation/', views.reservation, name='reservation'),
    path('menu/', views.menu_view, name='menu'),
    path('gallery/', views.gallery_view, name='gallery'), 

]
