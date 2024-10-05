from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_music, name='search_music'),
    path('download/<str:song_id>/', views.download_music, name='download_music'),
]
