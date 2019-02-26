from django.urls import path

from . import views
<!--ROUTING PATHS TO FUNCTIONS IN VIEWS-->
urlpatterns = [
    path('songs/', views.list_songs, name='list_songs'),
    path('songs/<int:song_id>/', views.list_song, name='song_details'),
    path('songs1/<int:song_id>/', views.lastdetails, name='lastdetails'),

]
