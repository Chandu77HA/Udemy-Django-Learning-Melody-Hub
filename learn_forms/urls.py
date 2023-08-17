from django.urls import path
from learn_forms import views

app_name = "learn_forms"

urlpatterns = [

    path('form_one/', views.form_one, name = 'form_one'),
    path('form_two/', views.form_two, name = 'form_two'),
    path('form_three/', views.form_three, name = 'form_three'),
    path('form_four/', views.form_four, name = 'form_four'),
    path('musician_form/', views.musician_form, name = 'musician_form'),


]
