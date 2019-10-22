from django.urls import path, include
from .views import *

app_name = 'books'

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('sold/',SoldView.as_view(),name = 'sold'),
    path('find/',FindView.as_view(),name = 'find'),

]