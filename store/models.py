from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# from django.db.models import Count

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=120) 
    description=models.CharField(max_length=500) 
    brand=models.CharField(max_length=200) 
    image=models.ImageField(upload_to="images",null=True)   
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=200) 

    def __str__(self):
        return self.name

class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    # @property
    # def question_answers(self):
    #     qs=self.answers_set.all().annotate(u_count=Count('rating')).order_by('-u_count')   
    #     return qs

    # @property
    # def ratingcount(self):
    #     return self.rating.all().count()

    # def __str__(self):
    #     return self.product

class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("removed","removed")
    )
    status=models.CharField(max_length=120,choices=options,default="In-cart")

    # def __str__(self):
    #     return self.product
