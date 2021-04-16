from django.shortcuts import render

def base(request):
    template = 'base.html'
    return render(request, template, {})

def index(request):
    template = 'index.html'
    return render(request, template, {} )

def about(request):
    template = 'about.html'
    return render(request, template, {} )

def services(request):
    template = 'services.html'
    return render(request, template, {} )

def contact(request):
    template = 'contact.html'
    return render(request, template, {} )

