from store.models import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta():
        model=Products
        feilds="__all__"