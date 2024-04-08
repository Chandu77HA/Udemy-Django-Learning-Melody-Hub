from django.urls import path
from music_album import views

app_name = "music_album"

urlpatterns = [

    path('list_musician/', views.list_musician, name='list_musician'),
    path('test_one/', views.test_one, name='test_one'),

    # CRUD Operation
    path('home_page/', views.home_page, name='home_page'),
    path('album_list/', views.album_list, name='album_list'),
    path('album_form/', views.album_form, name='album_form'),
    path('musician_list/', views.musician_list, name='musician_list'),
    path('musician_form/', views.musician_form, name='musician_form'),

    path('individual_album_list/<int:artist_id>/',
         views.individual_album_list, name='individual_album_list'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/',
         views.delete_album, name='delete_album'),
    path('delete_musician/<int:artist_id>/',
         views.delete_musician, name='delete_musician'),

    path('sample_file_details/', views.sample_file_details,
         name='disp_sample_file_details'),

]
