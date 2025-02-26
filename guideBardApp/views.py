from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import forms, authenticate
from django.forms.formsets import formset_factory
from django.contrib.auth import settings
from django.contrib.auth.models import User

def homePage(request):
    return render(request, 'home.html')

def signUp(request):
    return render(request, 'sign-up.html')

def login(request):
    return render(request, 'login.html')

def tourGuide(request):
    return render(request, 'tour-guide.html')

def reviews(request):
    return render(request, 'review.html')

def profile(request):
    return render(request, 'profile.html')

def contacts(request):
    return render(request, 'contacts.html')

def payment(request):
    return render(request, 'home.html')