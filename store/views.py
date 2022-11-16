from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.decorators import action

from store.serializer import ProductsSerializer,CartSerializer,ReviewSerilaizer
from store.models import Products,Carts
# Create your views here.

class ProductsView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductsSerializer
    queryset=Products.objects.all()

    @action(methods=["GET"],detail=False)
    def categories(self,request,*args,**kwargs):
        qs=Products.objects.values_list("category",flat=True).distinct()  
        # no duplicate values lists
        return Response(data=qs)

    def list(self,request,*args,**kwargs):
        qs=Products.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category=request.query_params.get("category"))
        serializer=ProductsSerializer(qs,many=True)
        return Response(data=serializer.data)

# localhost:8000/products/1/addto_cart/
    @action(methods=["post"],detail=True)
    def addto_cart(self,request,*args,**kw):
        product=self.get_object()
        user=request.user
        serializer=CartSerializer(data=request.data,context={"product":product,"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# localhost:8000/products/1/add_reviews/
    @action(methods=["post"],detail=True)
    def add_reviews(self,request,*args,**kwargs):
        product=self.get_object()
        user=request.user
        serializer=ReviewSerilaizer(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CartView(ViewSet):
    authentication_class=[authentication.TokenAuthentication]
    permission_class=[permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=Carts.objects.filter(user=request.user)
        serializer=CartSerializer(qs,many=True)
        return Response(data=serializer.data)