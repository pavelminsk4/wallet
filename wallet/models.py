from django.db import models
from django.core.exceptions import ValidationError


class Wallet(models.Model):
    label      = models.CharField(max_length=255)
    balance    = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValidationError("Wallet balance cannot be negative.")
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.label


class Transaction(models.Model):
    wallet     = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    tx_id      = models.CharField(max_length=64, unique=True)
    amount     = models.DecimalField(max_digits=18, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        wallet = self.wallet
        wallet.balance += self.amount
        wallet.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.tx_id
