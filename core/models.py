from __future__ import unicode_literals
from django.db import models


class Customer(models.Model):
    loan_amount = models.FloatField()
    number_of_years = models.IntegerField()
    interest_rate = models.FloatField()
    monthly_rate = models.FloatField()

    class Meta:
        db_table = "customer"
