from django.shortcuts import render
from .models import Car

def home(request):
    cars = Car.objects.all()

    makes = set([car.make for car in cars])

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
        'title':'Modern',
        'cars':final_cars,
        'makes':makes
    }

    return render(request, 'Sales/index.html', context)

def details(request, id):
    car = Car.objects.filter(id=id)
    car = car[0]

    photos = car.photos.replace("'",'').replace('[','').replace(']','').split(', ')
    if len(photos) >= 1 and photos[0] != '':
        main_photo = photos[0]
    else:
        main_photo = 'https://i.kym-cdn.com/entries/icons/facebook/000/021/572/maxresdefault.jpg'

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
    }

    context = {
        'title':car['title'],
        'car':car,
    }

    return render(request, 'Sales/details.html', context)

# def update(request):
#     from MyTools import MyTools as tools

#     Car.objects.all().delete()

#     with tools.driver(headless=1) as driver:
#         driver.get('https://duttongarage.com/prestige-cars')
#         pages = driver.execute_script('return document.querySelectorAll(".me-block.me-PanelCol.height-grow.me-max-width a.fresco")')
#         i = 0
#         links = []
#         while i < len(pages):
#             links.append(driver.execute_script(f'return document.querySelectorAll(".me-block.me-PanelCol.height-grow.me-max-width a.fresco")[{i}].href'))
#             i += 2

#     def get_details(link, links):
#         with open('test.txt', 'a') as f:
#             with tools.driver(headless=1) as driver:
#                 print(f'[SEARCHING] {link}')
#                 driver.get(link)

#                 photos = driver.execute_script('return document.querySelectorAll(".column.item.masonry")')
#                 results = Car( 
#                     make=driver.execute_script('return document.querySelector("h1.MEC12").innerText').split(' ')[1], 
#                     model=driver.execute_script('return document.querySelector("h1.MEC12").innerText'), 
#                     year=driver.execute_script('return document.querySelector("h1.MEC12").innerText').split(' ')[0], 
#                     price=driver.execute_script('return document.querySelector("h4.MEC12").innerText'), 
#                     mileage=driver.execute_script('return document.querySelectorAll("tbody tr")[1].querySelectorAll("td")[1].innerText'), 
#                     body_style=driver.execute_script('return document.querySelectorAll("tbody tr")[2].querySelectorAll("td")[1].innerText'), 
#                     fuel_type=driver.execute_script('return document.querySelectorAll("tbody tr")[3].querySelectorAll("td")[1].innerText'), 
#                     description=driver.execute_script('return document.querySelector(".me-block.me-Hamle p").innerText'), 
#                     photos=[driver.execute_script(f"""return document.querySelectorAll(".column.item.masonry")[{i}].querySelector("img").srcset.split(' ')[document.querySelectorAll(".column.item.masonry")[{i}].querySelector("img").srcset.split(' ').length - 2]""") for i in range(len(photos))])
#                 results.save()
                
#     results = []
#     tools.Thread(target=get_details, args=[results], iterator=links, max_workers=5)
#     home(request)