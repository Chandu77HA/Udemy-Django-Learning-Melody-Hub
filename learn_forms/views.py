from django.shortcuts import render
from music_album.models import Musician, Album
from music_album.views import list_musician
from learn_forms import forms


# Create your views here.

def form_one(request):
    form_data ={}
    return render(request, 'learn_forms/form_one.html', context=form_data)


def form_two(request):
    new_form = forms.UserForm()
    form_data ={'test_form' : new_form,
                'heading_1' :'This if form using djnago library'}
    
    if request.method == 'POST':
        the_from = forms.UserForm(request.POST)

        if the_from.is_valid():
            user_name = the_from.cleaned_data['user_name']
            user_dob = the_from.cleaned_data['user_dob']
            user_email = the_from.cleaned_data['user_email']

            form_data.update({'user_name':user_name})
            form_data.update({'user_dob':user_dob})
            form_data.update({'user_email':user_email})
            form_data.update({'form_submited':"Yes"})

    return render(request, 'learn_forms/form_two.html', context=form_data)


def form_three(request):
    new_form = forms.UserFormThree()
    form_data ={'test_form' : new_form,
                'heading_1' :'This if form using djnago library'}
    
    if request.method == 'POST':
        the_from = forms.UserFormThree(request.POST)

        if the_from.is_valid():
            form_data.update({'boolean_field' : the_from.cleaned_data['boolean_field']})
            form_data.update({'char_field' : the_from.cleaned_data['char_field']})
            form_data.update({'choice_field' : the_from.cleaned_data['choice_field']})
            form_data.update({'new_field' : the_from.cleaned_data['new_field']})
            form_data.update({'form_submited':"Yes"})

    return render(request, 'learn_forms/form_three.html', context=form_data)


def form_four(request):
    new_form = forms.UserFormFour()
    form_data ={'test_form' : new_form,
                'heading_1' :'This if form using djnago library'}
    
    if request.method == 'POST':
        the_from = forms.UserFormFour(request.POST)
        form_data.update({'test_form' : the_from})

        if the_from.is_valid():
            form_data.update({'name' : the_from.cleaned_data['name']})
            form_data.update({'number' : the_from.cleaned_data['number']})
            form_data.update({'new_field' : the_from.cleaned_data['new_field']})
            form_data.update({'form_submited':"Yes"})

    return render(request, 'learn_forms/form_four.html', context=form_data)



def form_five(request):
    new_form = forms.UserFormFive()
    form_data ={'test_form' : new_form,
                'heading_1' :'This if form using djnago library'}
    
    if request.method == 'POST':
        the_from = forms.UserFormFive(request.POST)
        form_data.update({'test_form' : the_from})

        if the_from.is_valid():
            form_data.update({'field' : "Fields Match !"})
            form_data.update({'form_submited':"Yes"})

    return render(request, 'learn_forms/form_five.html', context=form_data)


def musician_form(request):
    new_form = forms.MusicianForm()

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return list_musician(request)
        
    diction = {'pass_form' : new_form,
                'heading_1':'Add Musician Using Django Model Forms'}

    return render(request, 'learn_forms/musician_form.html', context=diction)

