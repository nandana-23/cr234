from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='app'),
    path('about',views.about,name='index')
]