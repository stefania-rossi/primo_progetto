from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "prima_app/homepage.html")

def welcome(request):
    return render(request, "prima_app/welcome.html")

def lista(request):
    return render(request, "prima_app/lista.html")

def chi_siamo(request):
    return render(request, "prima_app/chi_siamo.html")

def variabili(request):
    context = {
        'var1': 'Prima variabile',
        'var2': 'Seconda variabile',
        'var3': 'Terza varibiabile'
        #se ci sono variabili da passare all'html si crea un oggetto per gestirle meglio e + leeggibile
    }
    return render(request, "variabili.html" ,context)


def index(request):
    return render(request, "prima_app/index.html")

