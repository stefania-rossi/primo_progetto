from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormContatto,Contatto

'''
def contatti(request):
    form = FormContatto()
    context = {"form":form}
    return render(request, "contatto.html", context)

'''

def contatti(request):

    if request.method == "POST":
        form = FormContatto(request.POST)
        if form.is_valid():
        
         print("Il form è valido!")
         print("NOME: ", form.cleaned_data["nome"])
         print("COGNOME: ", form.cleaned_data["cognome"])
         print("EMAIL: ", form.cleaned_data["email"])
         print("CONTENUTO: ", form.cleaned_data["contenuto"])
         print("Salvo il contatto nel database")
         nuovo_contatto = form.save()
         print("new_post: ", nuovo_contatto)
         print(nuovo_contatto.nome)
         print(nuovo_contatto.cognome)
         print(nuovo_contatto.email)
         print(nuovo_contatto.contenuto)

         return HttpResponse("<h1>Grazie per averci contattato </h1>")

    else: 
        form = FormContatto

    context = {"form":form}
    return render(request, "contatto.html", context)


def lista_contatti(request):
    contatti = Contatto.objects.all()
    return render(request, "lista_contatti.html", {"contatti": contatti})
        