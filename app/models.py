from django.db import models

class Cars(models.Model):
    model = models.CharField(max_length=250)
    make = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=250)
    year = models.IntegerField() 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.model