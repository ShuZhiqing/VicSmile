from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/home.html', context={})


# def other(request):
#     return render(request, 'clinic/other.html', context={})