from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'mensaje': 'Bienvenido a la app de gatitos'
    }
    return render(
        request,
        'gatos/index.html',
        context
    )

def agregar(request):
    return render(
        request,
        'gatos/add.html'
    )

def listar(request):
    context = {
        'gatos': [
            {'nombre': 'Jinx', 'raza': 'Himalaya', 'edad': 1, 'genero': 'Hembra', 'color': 'Gris', 'peso': '3kg'},
            {'nombre': 'Belatrix', 'raza': 'Angora', 'edad': 5, 'genero': 'Hembra', 'color': 'Negro', 'peso': '5kg'},
            {'nombre': 'Aaron', 'raza': 'Siamés', 'edad': 2, 'genero': 'Macho', 'color': 'Blanco', 'peso': '3kg'},
            {'nombre': 'King', 'raza': 'Persa', 'edad': 9, 'genero': 'Macho', 'color': 'Rubio', 'peso': '6kg'}
        ]
    }
    return render(
        request,
        'gatos/list.html',
        context
    )