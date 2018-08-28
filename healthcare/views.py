from django.shortcuts import render


# Create your views here.
def system(request):
    return render(request, 'healthcare/system.html', context={})


def medicare(request):
    return render(request, 'healthcare/medicare.html', context={})


def rights(request):
    return render(request, 'healthcare/rights.html', context={})


def translation(request):
    return render(request, 'healthcare/translation.html', context={})


def community(request):
    return render(request, 'healthcare/community.html', context={})


def insurance(request):
    return render(request, 'healthcare/insurance.html', context={})


def healthcare(request):
    return render(request, 'healthcare/healthcare.html', context={})
