from .forms import UploadSamplFileForm
from django.shortcuts import render, redirect
from music_album.models import Musician, Album
from music_album import forms
from django.db.models import Avg

# Create your views here.


def list_musician(request):
    musician_list = Musician.objects.order_by('first_name')
    dict_data = {'text': "This is the list of Musicians",
                 'musician': musician_list}
    return render(request, 'music_album/musician.html', context=dict_data)


def test_one(request):
    data_passing = {'sample_text': 'Learning Template Inheritence',
                    'sample_data': 'Nav bar is from layout/base.html and Inherited in this page using template Inheritence',
                    'text_one': 'our perseption is our reality',
                    'text_two': 'WHAT YOU THINK YOU BECOME',
                    'text_three': '10',
                    'text_four': 'believe in yourself',
                    'text_five': 'django uses ORM',
                    'text_six': 'Get the Album data from admin',
                    'get_album': Album.objects.get(pk=1),
                    'text_seven': 'To check filters working - ',
                    }
    return render(request, 'music_album/test_one.html', context=data_passing)

# =============================================================================================================================
# CRUD Operation indjango


def home_page(request):
    album_data = {
        'title': 'Home Page',
    }
    return render(request, 'music_album/home.html', context=album_data)


def album_list(request):
    get_albums = Album.objects.order_by('artist')
    album_data = {
        'title': 'List of Albums',
        'album_list': get_albums,
    }
    return render(request, 'music_album/album_list.html', context=album_data)


def album_form(request):
    load_album_form = forms.AlbumForm()

    if request.method == 'POST':
        load_album_form = forms.AlbumForm(request.POST)

        if load_album_form.is_valid():
            load_album_form.save(commit=True)
            return album_list(request)

    album_data = {
        'title': 'Add Album',
        'album_form': load_album_form
    }
    return render(request, 'music_album/album_form.html', context=album_data)


def musician_list(request):
    get_musicians = Musician.objects.order_by('first_name')
    musician_data = {
        'title': 'List of Musicians',
        'musician_list': get_musicians,
    }
    return render(request, 'music_album/musician_list.html', context=musician_data)


def musician_form(request):
    load_musician_form = forms.MusicianForm()

    if request.method == 'POST':
        load_musician_form = forms.MusicianForm(request.POST)

        if load_musician_form.is_valid():
            load_musician_form.save(commit=True)
            return musician_list(request)

    album_data = {
        'title': 'Add Musician',
        'musician_form': load_musician_form,

    }
    return render(request, 'music_album/musician_form.html', context=album_data)


def individual_album_list(request, artist_id):
    get_artist_info = Musician.objects.get(pk=artist_id)
    get_album_list = Album.objects.filter(artist=artist_id).order_by('name')
    get_artist_rating = Album.objects.filter(
        artist=artist_id).aggregate(Avg('num_stars'))
    album_data = {
        'title': 'Individual Album List',
        'artist_info': get_artist_info,
        'ind_album_list': get_album_list,
        'artist_rating': get_artist_rating,
    }
    return render(request, 'music_album/individual_album_list.html', context=album_data)


def edit_artist(request, artist_id):
    get_artist_info = Musician.objects.get(pk=artist_id)
    get_artist_form = forms.MusicianForm(instance=get_artist_info)
    artist_data = {'title': 'Edit Artist', }

    if request.method == 'POST':
        get_artist_form = forms.MusicianForm(
            request.POST, instance=get_artist_info)

        if get_artist_form.is_valid():
            get_artist_form.save(commit=True)
            artist_data.update(
                {'success_text': 'Artist Data Successfully Updated !'})
            return individual_album_list(request, artist_id)

    artist_data.update({'edit_from': get_artist_form, })
    return render(request, 'music_album/edit_artist.html', context=artist_data)


def edit_album(request, album_id):
    get_album_info = Album.objects.get(pk=album_id)
    get_album_form = forms.AlbumForm(instance=get_album_info)
    album_data = {'title': 'Edit Album', }

    if request.method == 'POST':
        get_album_form = forms.AlbumForm(request.POST, instance=get_album_info)

        if get_album_form.is_valid():
            get_album_form.save(commit=True)
            album_data.update({'success_text': 'Album Successfully Updated !'})

    album_data.update({'edit_from': get_album_form, })
    album_data.update({'album_id': album_id, })
    return render(request, 'music_album/edit_album.html', context=album_data)


def delete_album(request, album_id):
    get_album_to_delete = Album.objects.get(pk=album_id).delete()
    delete_album_data = {'delete_success': 'Album Deleted Successfully !'}
    return render(request, 'music_album/delete_page.html', context=delete_album_data)


def delete_musician(request, artist_id):
    get_musician_to_delete = Musician.objects.get(pk=artist_id).delete()
    delete_musician_data = {
        'delete_success': 'Musician Deleted Successfully !'}
    return render(request, 'music_album/delete_page.html', context=delete_musician_data)


def sample_file_details(request):
    if request.method == 'POST':
        form = UploadSamplFileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            form.save()
            return redirect('home_page')

    form = UploadSamplFileForm()
    return render(request, 'music_album/select_headers.html', {'form': form})


# def dexma_app_cred_home(request):
#     if request.method == "POST":,
#         app_id = request.POST.get("dexma_app_id", ' ').strip()
#         app_secret_id = request.POST.get("dexma_app_secret_id", ' ').strip()
#         app_cred = DexmaAppCredentials.objects.first()
#         if app_cred:
#             app_cred.dexma_app_id = app_id
#             app_cred.dexma_app_secret_id = app_secret_id
#             app_cred.save()
#         else:
#             app_cred = DexmaAppCredentials(
#                 dexma_app_id=app_id, dexma_app_secret_id=app_secret_id)
#             app_cred.save()
#         return redirect('display_dexama_app_cred')
#     return render(request, "test_app/dexma_app_cred_submit.html")
