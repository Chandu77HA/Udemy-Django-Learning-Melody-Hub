from django import forms
from django.core import validators
from music_album.models import Album, Musician

class UserForm(forms.Form):
    user_name = forms.CharField(label="User Name", widget = forms.TextInput(attrs={'placeholder' : 'Enter your Full Name', 'style':'width:300px'}))
    user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput(attrs={'type' : 'date'}))
    user_email = forms.EmailField(label="User Email", widget = forms.TextInput(attrs={'placeholder' : 'Enter Email'}))

class UserFormThree(forms.Form):
    boolean_field = forms.BooleanField(required=False)
    char_field = forms.CharField(max_length=20, min_length=5)
    choice_field = forms.ChoiceField(choices=(('', 'Select'),('1', 'First'),('2', 'Two'),('3', 'Three'),('4', 'Four')))
    choices = (('Apple', 'A'), ('Ball', 'B'), ('Cat', 'C'), ('Dog', 'D'))
    new_field = forms.ChoiceField(choices = choices, widget=forms.RadioSelect)

class UserFormFour(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
    number = forms.IntegerField(validators=[validators.MaxValueValidator(10), validators.MinValueValidator(5)])
    choices = (('Apple', 'A'), ('Ball', 'B'), ('Cat', 'C'), ('Dog', 'D'))
    new_field = forms.ChoiceField(choices = choices, widget=forms.RadioSelect)
    
class UserFormFive(forms.Form):
    user_email = forms.EmailField()
    user_vmail = forms.EmailField()

    def clean(self):
        all_data_cleaned = super().clean()
        user_email = all_data_cleaned['user_email']
        user_vmail = all_data_cleaned['user_vmail']

        if user_email != user_vmail:
            raise forms.ValidationError("Field Dont Match")

# Django model Forms

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"