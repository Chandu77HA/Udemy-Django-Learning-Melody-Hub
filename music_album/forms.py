from django import forms
from music_album.models import Album, Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget = forms.TextInput(attrs={'type' : 'date'}))
    class Meta:
        model = Album
        fields = "__all__"