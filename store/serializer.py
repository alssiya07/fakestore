from store.models import Products,Carts,Reviews
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta():
        model=Carts
        fields=["id","product","user","date"]
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(user=user,product=product,**validated_data)

class ReviewSerilaizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta():
        model=Reviews
        fields=["id","comment","rating","product","user"]

    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Reviews.objects.create(**validated_data,user=user,product=product)

class ProductsSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    product_reviews=ReviewSerilaizer(read_only=True,many=tuple)
    avg_rating=serializers.IntegerField(read_only=True)

    class Meta():
        model=Products
        fields=["id","name","description","category",
        "price","image","avg_rating","product_reviews"]



