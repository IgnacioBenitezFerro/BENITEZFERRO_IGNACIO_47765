from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#La funcionalidad será de la siguiente manera. Tanto seller como Market propondran ofertas de tikcer o tambien llamadas posiciones, donde los Buyers tomaran la decisión de comprar.

class Buyer(models.Model):
    
    
    def __str__(self):
        
        return f"Asker: {self.nombre} {self.apellido} --- Offers: {self.ticker} at market price {self.precio}"
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    ticker = models.CharField(max_length=5)
    precio = models.FloatField(max_length=4)

class Seller(models.Model):
    
    
    def __str__(self):
        
        return f"Bidder: {self.nombre} {self.apellido} --- Offers: {self.ticker} at market price {self.precio}"
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    ticker = models.CharField(max_length=5)
    precio = models.FloatField()

class Market(models.Model):
    
    def __str__(self):
        
        return f"Position: {self.position} --- Ticker: {self.ticker}"
    
    
    position = models.CharField(max_length=30)
    ticker = models.CharField(max_length=5)
    price = models.FloatField(max_length=1000000)
    
 
class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"
