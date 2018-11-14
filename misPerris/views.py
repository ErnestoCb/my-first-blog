from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import perro
from django.contrib.auth.decorators import login_required
from .forms import perroForm

# Create your views here.
def home(request):
    return render(request, 'misPerris/homePerro.html', {})

def perro_list(request):
    return render(request, 'misPerris/listarPerro.html', {})

def perro_detail(request, pk):
    perros = get_object_or_404(perro, pk=pk)
    return render(request, 'misPerris/perro_detail.html', {'perros': perros})