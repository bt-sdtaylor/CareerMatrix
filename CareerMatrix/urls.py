from django.urls import path

from .views import indexView, pathView

app_name = 'CareerMatrix'

urlpatterns = [
    path('', indexView, name='index'),
]
