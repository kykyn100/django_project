from django.shortcuts import render
from datetime import datetime


# Create your views here.

def index(request):
    menu_points = [
        {'menu_point': '/', 'name': 'домой'},
        {'menu_point': '/products/', 'name': 'продукты'},
        {'menu_point': '/contact/', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/index.html', context={
        'menu_points': menu_points,
        'act_date': datetime.now(),
    })


def contact(request):
    menu_points = [
        {'menu_point': '/', 'name': 'домой'},
        {'menu_point': '/products/', 'name': 'продукты'},
        {'menu_point': '/contact/', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/contact.html', context={
        'menu_points': menu_points,
        'act_date': datetime.now(),
    })

def products(request):
    menu_points = [
        {'menu_point': '/', 'name': 'домой'},
        {'menu_point': '/products/', 'name': 'продукты'},
        {'menu_point': '/contact/', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/products.html', context={
        'menu_points': menu_points,
        'act_date': datetime.now(),
    })
