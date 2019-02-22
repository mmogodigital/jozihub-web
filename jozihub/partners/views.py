from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'partners/partners.html', context)