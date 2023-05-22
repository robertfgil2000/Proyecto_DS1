from django.db import models
#con estos modelos el gerente puede crear sucursales y otros roles
# Create your models here.

#direccion sucursal
class Address(models.Model):
    street = models.CharField(max_length = 40)
    city = models.CharField(max_length = 60)
    active = models.BooleanField()
    country = models.CharField(max_length = 60)

#sucursal
class Office(models.Model):
    name= models.CharField(max_length=30)
    #Llave foranea a adress_id
    office_id = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)

#cuenta para hacer login
class Account(models.Model):
    email= models.EmailField(max_length=50, unique = True)
    password = models.CharField(max_length=20, unique= True)

    def __str__(self):
        return 'email: %s pass: %s' %(self.email, self.password) 

#jefe de taller
class BossWorkshop(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #llave foranea con sucursal
    office_id = models.ForeignKey(Office, null=True, blank=True, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account,null=True, blank=True, on_delete=models.CASCADE)

#vendedor
class Seller(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #llave foranea a office
    office_id = models.ForeignKey(Office, null=True, blank=True, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account,null=True, blank=True,on_delete=models.CASCADE)
