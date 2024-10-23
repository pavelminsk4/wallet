from rest_framework import viewsets, filters
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from rest_framework_json_api.pagination import JsonApiPageNumberPagination


class CustomPagination(JsonApiPageNumberPagination):
    page_query_param = 'page_number'
    page_size_query_param = 'page_length'
    page_size = 2
    max_page_size = 100


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class =  WalletSerializer
    pagination_class = CustomPagination


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = CustomPagination
