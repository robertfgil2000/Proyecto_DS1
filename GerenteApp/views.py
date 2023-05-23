from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import SellerSerializer
from .models import Office, Address, Seller

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
    
class SellerView(viewsets.ModelViewSet):
    serializer_class =  SellerSerializer
    queryset = Seller.objects.all()
