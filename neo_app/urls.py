from django.urls import path
from . import views

app_name= 'neo_app'

urlpatterns = [
    path('', views.neo_home, name='neo_home'),
    path('neo_search', views.neo_search, name='neo_search'),
    path('neo_result', views.neo_result, name='neo_result'),
]