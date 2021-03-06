from django.shortcuts import render
from Sales.models import Car

def home(request):
    cars = Car.objects.filter(is_classic=True)

    makes = sorted(set([car.make for car in cars]))

    final_cars = []

    for car in cars:
        photos = car.photos.replace("'",'').replace('[','').replace(']','').split(', ')
        if len(photos) >= 1 and photos[0] != '':
            main_photo = photos[0]
        else:
            main_photo = 'https://i.kym-cdn.com/entries/icons/facebook/000/021/572/maxresdefault.jpg'
        
        final_cars.append({
            'id':car.id,
            'make':car.make,
            'model':car.model,
            'year':car.year,
            'price':car.price,
            'mileage':car.mileage,
            'body_style':car.body_style,
            'fuel_type':car.fuel_type,
            'description':car.description,
            'main_photo':main_photo,
            'photos':photos,
        })

    context = {
        'title':'Classic',
        'cars':final_cars,
        'makes':makes,
        'header':'https://images7.alphacoders.com/301/301642.jpg'
    }

    return render(request, 'Sales/index.html', context)