from django.db import models

# Create your models here.

# Guest -- Movie -- reservation

class Movie(models.Model):
    hall=models.CharField(max_length=10 )
    movie=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return self.movie
    
class Guest(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    
    
    def  __str__(self):
        return self.name

class Reservation(models.Model):
    guest=models.ForeignKey(Guest, on_delete=models.CASCADE , related_name="reservation")
    movie=models.ForeignKey(Movie ,  related_name='reservation' , on_delete=models.CASCADE)
    seat=models.CharField(max_length=100)
    
    