from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
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
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['label', 'balance']
    ordering_fields = ['label', 'balance']


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['tx_id', 'amount']
    ordering_fields = ['tx_id', 'amount']
