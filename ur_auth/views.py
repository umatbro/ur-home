from django.shortcuts import render


def home(request):
    return render(request, 'ur_auth/home.html')


def login(request):
    pass
