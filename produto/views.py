from django.shortcuts import render
from django.http import HttpResponse
from produto.models import*
# Create your views here.


def Home(request):
    return render(request, "home.html")

def Index(request):
    lista = Produto.objects.all()
    context = {'produtos' : lista}
    return render(request, "index.html", context)

def Detalhar(request, id):
    produto = Produto.objects.get(id=id)
    context = {'produto' : produto}
    return render(request, "detalhar.html", context)

def Nos(request):
    return render (request, "sobrenos.html")
