from django.shortcuts import render

def index(request):
    return render(request, 'lab7app/index.html')
