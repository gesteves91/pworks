from django.urls import path

from . import views

urlpatterns = [
    path('subways', views.subways, name='subways'),
    path('subways/<str:subway_id>', views.subway_stops, name='subway_stops'),
]
