from django.shortcuts import render, get_object_or_404
from .models import Museo,Opera,Autore

# Create your views here.
def homepage(request):
    musei= Museo.objects.all() 

    context={"musei":musei}
    print (context)
    return render(request, "homepage.html", context)

def museoDetailView(request,pk):
    museo=get_object_or_404(Museo, pk=pk)
    opere=Opera.objects.filter(museo_id=pk)
    context={"museo": museo,
             "opere": opere}
    return render(request, "dettagli_museo.html", context)

def autoreDetailView(request,pk):
    autore=get_object_or_404(Autore, pk=pk)
    context={"autore": autore}
    return render(request, "dettagli_autore.html", context)
