from django.shortcuts import render


# Create your views here.
def result(request):
    return render(request, 'clinic/result.html', context={})
