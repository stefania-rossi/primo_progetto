from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo,Giornalista
import datetime

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "news/homepage.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo":articolo}
    return render(request, "articolo_detail.html", context)
    """"
    a = [] 
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    
    response = str(a) + "<br>" +  str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")
"""
"""
   a = ""
   g = ""
   for art in Articolo.objects.all():
      a += (art.titolo + "<br>")
   for gio in Giornalista.objects.all():
      g += (gio.nome + "<br>")
   response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g

   return HttpResponse("<h1>" + response + "</h1>")
"""

def listaArticoli(request, pk=None):
    trovato = False
    is_vuota = False
    if pk is None:
        articoli = Articolo.objects.all()
    else:
        trovato = True
        articoli = Articolo.objects.filter(giornalista_id=pk)
    if not articoli:
        is_vuota=True
    context = {
        'trovato':trovato,
        'articoli': articoli, 
        'is_vuota':is_vuota
    }
    return render(request, 'lista_articoli.html',context)  

def index4(request):
    return render(request, "index4.html")

def queryBase(request):
    articoli_cognome = Articolo.objects.filter(giornalista_cognome='Rossi')
    numero_totale_articoli=Articolo.objects.count()

    giornalista_1=Giornalista.objects.get(id=1)
    numero_articoli_giornalista_1= Articolo.objects.filter(giornalista=giornalista_1).count()

    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni = 0)

    articoli_più_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()

    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1900, 1, 1))

    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023,1,1))

    articoli_periodo = Articolo.objects.filter(data__range=(datetime.date(2023,1,1), datetime.date(2023,12,31)))

    giornalisti_nati= Giornalista.objects.filter(anno_di_nascita___lt=datetime.date(1980,1,1))
    articoli_giornalisti=Articolo.objects.filter(giornalista__in=giornalisti_nati)

    giornalista_giovane = Giornalista.object.order_by('anno di nascita').first()

    giornalista_anziano = Giornalista.objects.order_by('anno di nascita').first()

    ultimi = Articolo.objects.order_by('-data')[:5]

    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)