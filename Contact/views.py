from django.shortcuts import render

def home(request):
    context = {
        'title':'Contact Us',
        'header':'https://wallpapercave.com/wp/wp1927797.jpg'
    }
    return render(request, 'Contact/base.html', context)