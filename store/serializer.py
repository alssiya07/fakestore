from store.models import Products,Carts
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta():
        model=Products
        fields="__all__"

class CartSerializer(serializers.ReadOnlyField):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields=["product","user","date"]
    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("products")
        return Carts.objects.create(
            **validated_data,user=user,
            product=product)
