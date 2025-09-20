from django.shortcuts import render

from .models import Bead

def home(request):
    beads = Bead.objects.all()
    return render(request, 'logika/start1.html', {'beads':beads})

