from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import usuario, perro
from django.contrib.auth.decorators import login_required
from .forms import usuarios, perroForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = usuarios(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('home')
    else:
        form = usuarios()
    return render(request, 'misPerris/homePerro.html', {'form': form})

def perro_list(request):
    return render(request, 'misPerris/listarPerro.html', {})

def perro_detail(request, pk):
    perros = get_object_or_404(perro, pk=pk)
    return render(request, 'misPerris/perro_detail.html', {'perros': perros})