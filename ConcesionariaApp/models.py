from django.db import models

from GerenteApp.models import Office, Account

# Create your models here.
class Gerente(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    #llave foranea con Office que esta en models.py de Gerente.py
    office_gerente = models.ForeignKey(Office, null=True, blank = True, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account,null=True, blank=True, unique= True, on_delete=models.CASCADE)

    def __str__(self):
       return 'nombre completo: %s %s email: %s pass: %s' %(self.name, self.last_name, self.account_id.email, self.account_id.password) 


