from django.shortcuts import render

#wiew_a
def listaMaterie(request):
    context = {
        'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render(request, "voti/lista_materie.html", context)

#wiew_b
def votiStudenti(request):
    context = {
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request, "voti/voti_studenti.html", context)

#wiew_c
def mediaStudenti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    medie={}
    for studente,voti in voti.items():
        sum=0
        i=0
        for materia,voto,assenza in voti:
            sum += voto
            i += 1
        medie[studente] = sum/i
    
    context = {
        'medie' : medie
    }
    return render(request,"voti/media_studenti.html",context)

#wiew_d
def maxMinVoti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    max = 0
    mMax = []
    sMax =  []

    min = 100
    mMin = []
    sMin =  []
    for studente, voti in voti.items():
        for materia, voto, assenza in voti:
            if voto > max:
                max = voto
            if voto < min:
                min = voto

    for studente, voti in voti.items():
        for materia, voto, assenza in voti:
            if voto == max:
                mMax.append[materia]
                sMax.append[studente]
            if voto == min:
                mMin.append[materia]
                sMin.append[studente]
       

    context = {
        'max': max,
        'mMax' : mMax,
        'sMax' : sMax,
        'min': min,
        'mMin' : mMin,
        'sMin' : sMin
    }
    return render(request,"voti/max_min_voti.html", context)


def index_5(request):
    return render(request, "voti/index_5.html")