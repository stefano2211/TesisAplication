from django.db import models
from django.db.models import Q



class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class MoneyCategory(models.Model):
    name = models.CharField(max_length=200)

# Create your models here.
class CodeBank(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.CharField(max_length=200)

class CodeExpenses(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class CodeIncome(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()



class Expenses(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    typeBank = models.CharField(max_length=200)
    typeExpenses = models.CharField(max_length=200)
    typeMoney = models.CharField(max_length=200)
    date = models.DateField()
    dolar = models.FloatField(null=True)



class Income(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    typeBank = models.CharField(max_length=200)
    typeIncome = models.CharField(max_length=200)
    typeMoney = models.CharField(max_length=200)
    date = models.DateField()
    dolar = models.FloatField()
