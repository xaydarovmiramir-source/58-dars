from .views import home,fakultet,kafedra,fanlar,ustozlar,talabalar
from django.urls import path
urlpatterns=[path('',home,name='home'),
             path('fakultet/',fakultet,name='fakultet'),
             path('kafedra/',kafedra,name='kafedra'),
             path('fanlar/',fanlar,name='fanlar'),
             path('ustozlar/',ustozlar,name='ustozlar'),
             path('talabalar/',talabalar,name='talabalar')]