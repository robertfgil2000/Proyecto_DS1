from django.contrib import admin
from ConcesionariaApp.models import Gerente
from GerenteApp.models import Account

#el administrador crea gerente
# Register your models here.
admin.site.register(Gerente)
admin.site.register(Account)
