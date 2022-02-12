from django.urls import path
from . import views

app_name='Search_app'

urlpatterns=[

    path('search/',views.SearchResult,name='SearchResult'),
]