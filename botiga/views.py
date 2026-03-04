from django.shortcuts import render, redirect
from .models import Videojoc
from .forms import VideojocForm

def gestio_videojocs(request):
    videojocs = Videojoc.objects.all().order_by('titol')
    
    if request.method == "POST":
        form = VideojocForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestio_videojocs')
    else:
        form = VideojocForm()
    
    return render(request, 'botiga/gestio_videojocs.html', {
        'videojocs': videojocs,
        'form': form
    })
