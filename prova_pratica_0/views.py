from django.shortcuts import render
import random
# Create your views here.
def index_prova(request):
    return render (request, "prova_pratica_0/index_prova.html")

def somma(request):

    var1 = random.randint(1,10)
    var2 = random.randint(1,10)
    somma =  var1 + var2
     
    context = {
        'var1' : var1,
        'var2' : var2,
        'somma' : somma
    }

    return render (request, "prova_pratica_0/somma.html", context)

def media(request):
    lista=[]
    x = 0
    totale = 0
    n = 0
    media = 0
    while x <= 30:
      lista.append(random.randint(1,10))
      x += 1
    for num in lista:
        totale += num
        n += 1
    media = totale/n


    
    context = {
        'lista' : lista,
        'media' : media
    }

    return render(request, "prova_pratica_0/media.html", context)
