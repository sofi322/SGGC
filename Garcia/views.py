from django.shortcuts import render

def inicio(request):
    return render(request, "Garcia/inicio.html")
def registro(request):
    return render(request, "Garcia/formregistro.html")