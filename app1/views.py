from django.shortcuts import render

# Create your views here.
def recetas(request):
    lista=[
        {"tarta":"una deliciosa tarta","paella":"un clasico plato"}
    ]
    return render('app1/interfaz.html',lista)