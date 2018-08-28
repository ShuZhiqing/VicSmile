from django.shortcuts import render


# Create your views here.
def result(request):
    return render(request, 'clinic/result.html', context={})


def clinic(request):
    return render(request, 'clinic/clinic.html', context={})


def map(request):
    return render(request, 'clinic/map.html', context={})