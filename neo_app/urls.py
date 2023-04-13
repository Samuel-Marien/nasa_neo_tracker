from django.urls import path
from . import views

app_name= 'neo_app'

urlpatterns = [
    path('', views.neo_home, name='neo_home'),
    path('apod_search', views.apod_search, name='apod_search'),
    path('apod_result', views.apod_result, name='apod_result'),
    path('neo_search', views.neo_search, name='neo_search'),
    path('neo_result', views.neo_result, name='neo_result'),
    path('neo_detail/<int:neoId>', views.neo_detail, name='neo_detail'),
]