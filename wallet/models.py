from django.db import models


class Wallet(models.Model):
    label      = models.CharField(max_length=255)
    balance    = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    wallet     = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    tx_id      = models.CharField(max_length=64, unique=True)
    amount     = models.DecimalField(max_digits=18, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

