from decimal import Decimal
import datetime

from django.contrib import messages
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.core.validators import MinValueValidator


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.capitalize()

    def get_absolute_url(self):
        return reverse('item')


class Bank(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250)
    opening_bal_date = models.DateField()
    opening_bal = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('banks')


class Expenditure(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='items')
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=False, null=False, default=datetime.date.today)
    amount = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    remarks = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        template = '{0.item}, {0.date}'
        return template.format(self)

    def get_absolute_url(self):
        return reverse('expenditure_detail',kwargs={'pk':self.pk})
