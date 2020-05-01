from django.shortcuts import render

def home(request):
    context = {
        'title':'About',
        'header':'https://wallpaperplay.com/walls/full/e/d/5/250328.jpg'
    }

    return render(request, 'About/base.html', context)