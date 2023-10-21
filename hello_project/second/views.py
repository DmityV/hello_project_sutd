from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def second_page(request):
    template_name = 'second/second_page.html'
    return render(request, template_name)