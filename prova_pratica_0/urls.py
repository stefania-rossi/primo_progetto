from django.urls import path
from prova_pratica_0.views import index_prova, somma, media

app_name="prova_pratica_0"
urlpatterns=[
    path('index_prova',index_prova,name='index_prova'),
    path('somma',somma,name='somma'),
    path('media',media,name='media')
]