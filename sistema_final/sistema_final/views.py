from django.shortcuts import render
from .forms import LocalidadForm

def cargar_localidad(request):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario
            pass
    else:
        form = LocalidadForm()

    return render(request, 'form.html', {'form': form})
