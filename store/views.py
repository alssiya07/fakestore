from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions,authentication
from store.serializer import ProductsSerializer
from store.models import Products
# Create your views here.

class ProductsView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductsSerializer
    queryset=Products.objects.all()