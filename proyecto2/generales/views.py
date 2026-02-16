from django.shortcuts import render

# Create your views here.
# render devuelve un objeto de respuesta de Django que puede contener un archivo
def index(request):
    return render(request, "index.html")
