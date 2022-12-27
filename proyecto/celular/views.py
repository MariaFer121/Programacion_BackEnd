from django.shortcuts import render

# Create your views here.


def home (request):
    context = {
        'mensaje':'Bienvenido a la Formativa Unidad 1 - Programación Back End'
    }

    return render(
        request,
        'celular/templates/home.html',
        context
        )

def celulares (request):
    context = {
        'celulares' : [
            {'marca':'xiaomi', 'modelo':'redmi note 9', 'año':2019, 'fecha':'05/06/19'},
            {'marca':'iphone', 'modelo':'13 pro max', 'año':2022, 'fecha':'22/11/22'},
            {'marca':'xiaomi', 'modelo':'redmi note 10', 'año':2021, 'fecha':'03/12/21'},
            {'marca':'motorola', 'modelo':'moto g10', 'año':2022, 'fecha':'05/09/22'},
            {'marca':'xiaomi', 'modelo':'T12', 'año':2022, 'fecha':'08/03/22'},
            {'marca':'lg', 'modelo':'g7 plus', 'año':2019, 'fecha':'17/04/19'},
            {'marca':'xiaomi', 'modelo':'redmi note 11 pro g5', 'año':2022, 'fecha':'15/05/22'},
        ]
    }

    return render(
        request,
        'celular/templates/celulares.html',
        context
        )

def formulario (request):
    
    return render(
        request,
        'celular/templates/formulario.html'
        )