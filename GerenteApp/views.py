from django.shortcuts import render, redirect
from .models import Office, Address

# Create your views here.
def sucursal(request):   
    return render(request, "GerenteApp/sucursal_crear.html")

def crear_sucursal(request):
    office = Office(name=request.POST['name_sucursal'])
    address = Address(street=request.POST['street'], city=request.POST['city'], active=request.POST['activo'], country=request.POST['country'])

    office.save()
    address.save()

    #print(request.POST) #enviar datos metodo post
    return redirect('/gerente/sucursal/')
    


