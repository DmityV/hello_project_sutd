from django.urls import path
from . import views

app_name = 'second'

urlpatterns = [
    path('', views.second_page, name="second_page"),
]
