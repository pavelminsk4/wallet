from django.contrib import admin
from .models import Wallet, Transaction


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'balance', 'created_at', 'updated_at')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'wallet', 'tx_id', 'amount',
                    'created_at', 'updated_at')


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
