from django.shortcuts import render


def index(request):
    context = {
        'slogan': 'super deal',
        'user': 123,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contact.html')
