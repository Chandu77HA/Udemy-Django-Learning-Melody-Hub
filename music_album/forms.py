from django import forms
from music_album.models import Album, Musician, UploadSamplFile
from django.forms.widgets import ClearableFileInput


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Album
        fields = "__all__"


class UploadSamplFileForm(forms.ModelForm):
    file_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'file_name', 'style': 'width: 300px;', 'class': 'form-control'}))
    sample_file = forms.FileField(widget=ClearableFileInput(
        attrs={'class': 'form-control', 'style': 'width: 1000px;', 'accept': '.pdf'}), max_length=600)

    class Meta:
        model = UploadSamplFile
        fields = '__all__'
