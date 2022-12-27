from django.shortcuts import render

# Create your views here.


def home (request):
    context = {
        'mensaje':'Bienvenido a la Evaluacion N°1 - Zapatillas'
    }

    return render(
        request,
        'zapatillas/templates/home.html',
        context
        )

def zapatillas (request):
    context = {
        'zapatillas' : [
            {'marca':'adidad', 'modelo':'M001', 'color':'negro', 'talla':'38'},
            {'marca':'nike', 'modelo':'MaxPro23', 'color':'lila', 'talla':'42'},
            {'marca':'puma', 'modelo':'Model124', 'color':'blanco', 'talla':'34'},
            {'marca':'nike', 'modelo':'GT 4.0', 'color':'gris', 'talla':'36'},
            {'marca':'converce', 'modelo':'gastadas', 'color':'cafe', 'talla':'44'},
        ]
    }

    return render(
        request,
        'zapatillas/templates/zapatillas.html',
        context
        )

def formulario (request):
    
    return render(
        request,
        'zapatillas/templates/formulario.html'
        )