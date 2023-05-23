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



class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(200)
    name = models.CharField(200) 
    phone = models.CharField(200)
    password = models.CharField(200)  

    

    def _str_(self):
        return self.email
    
    @staticmethod
    def user_create(email: str, name: int, phone: str, password:str):
        user = User(email=email, name=name, phone=phone, password=password)
        user.save()
        return user
    
    def user_modify(self, email: str = None, name: int = None, 
                             phone: str = None, password: str = None):
        if email!=None:
            self.email = email
        if name!=None:
            self.name = name
        if phone!=None:
            self.phone = phone
        if password!=None:
            self.password = password
        self.save()
        
    def user_delete(self):
        self.delete()
    
    @staticmethod
    def user_get_all():
        user = User.objects.all()
        return user
    
    @staticmethod
    def user_get(user_id: int):
        user = User.objects.get(user_id=user_id)
        return user

    @staticmethod
    def user_get_by_email(email: str, password):
        user = User.objects.get(email=email)
        response = password == user.password
        if response:
            return user
        else:
            return False
