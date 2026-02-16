from django.urls import path
from voti.views import votiStudenti,listaMaterie,mediaStudenti,maxMinVoti,index_5
app_name="voti"
urlpatterns=[  
    path('lista_materie', listaMaterie, name = 'lista_materie'),
    path('voti_studenti', votiStudenti, name='voti_studenti'),
    path('media_studenti', mediaStudenti, name='media_studenti'),
    path('max_min_voti', maxMinVoti, name = 'max_min_voti'),
    path('', index_5, name='index_5')
]
