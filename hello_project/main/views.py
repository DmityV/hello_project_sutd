from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index_page(request):
    template_name = 'main/index.html'
    return render(request, template_name)