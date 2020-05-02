from django.shortcuts import render
from Sales.models import Car
from Sales.views import home as sales_home

def home(request):
    return sales_home(request)

def details(request, id):
    car = Car.objects.filter(id=id)
    car = car[0]

    photos = car.photos.replace("'",'').replace('[','').replace(']','').split(', ')
    if len(photos) >= 1 and photos[0] != '':
        main_photo = photos[0]
    else:
        main_photo = 'https://i.kym-cdn.com/entries/icons/facebook/000/021/572/maxresdefault.jpg'

    if car.is_classic == True:
        header = 'https://images7.alphacoders.com/301/301642.jpg'
    else:
        header = False

    car = {
        'id':car.id,
        'title':f'{car.year} {car.make} {car.model}',
        'make':car.make,
        'model':car.model,
        'year':car.year,
        'price':car.price,
        'mileage':car.mileage,
        'body_style':car.body_style,
        'fuel_type':car.fuel_type,
        'description':car.description.replace('\n','\n '),
        'main_photo':main_photo,
        'photos':photos,
        'is_classic':car.is_classic
    }

    context = {
        'title':car['title'],
        'car':car,
        'header':header
    }

    return render(request, 'Sales/details.html', context)