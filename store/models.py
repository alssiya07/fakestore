from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200,unique=True) 
    description=models.CharField(max_length=500) 
    brand=models.CharField(max_length=200)    
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    category=models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Reviews(models.Model):
    product=models.ForeignKey(Product)
    user=models.ForeignKey(User)
    comment=models.CharField(max_length=500)
    rating=models.ManyToManyField(User,related_name="rating")

    @property
    def question_answers(self):
        qs=self.answers_set.all().annotate(u_count=Count('rating')).order_by('-u_count')   
        return qs

    @property
    def ratingcount(self):
        return self.rating.all().count()

    def __str__(self):
        return self.product

class Carts(models.Model):
    product=models.ForeignKey(Product)
    user=models.ForeignKey(User)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product