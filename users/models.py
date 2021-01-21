from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    
# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    current_balance = models.FloatField(validators=[MinValueValidator(3000.00)])

    def __str__(self):
        return self.first_name

class Transfer(models.Model):
    tx_from = models.ForeignKey(Customers, related_name="tx_from", on_delete=models.CASCADE, null=True)
    tx_to = models.ForeignKey(Customers, related_name="tx_to", on_delete=models.CASCADE, null=True)
    amount = models.FloatField(validators=[MaxValueValidator(100000.00)])
    time=models.DateTimeField(auto_now_add=True)