from django.urls import path
from voti.views import voti_studenti,lista_materie,media_studenti,max_min_voti,index_5
app_name="seconda_app"
urlpatterns=[  
    path('lista_materie', lista_materie, name = 'lista_materie'),
    path('voti_studenti', voti_studenti, name='voti_studenti'),
    path('media_studenti', media_studenti, name='media_studenti'),
    path('max_min_voti', max_min_voti, name = 'max_min_voti'),
    path('index_5', index_5, name='index_5')
]
