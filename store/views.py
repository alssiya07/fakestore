from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.decorators import action

from store.serializer import ProductsSerializer,CartSerializer
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

    @action(methods=["POST"],detail=True)
    def addto_cart(self,requst,*args,**kwargs):

        product=self.get_object()
        user=requst.user
        serializer=CartSerializer(
            data=requst.data,
            context={"user":user,"product":product}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)