from django.db import models

# Create your models here.
BRAND_CHOICES = (
    ('Nike', "Nike"),
    ('Adidas', "Adidas"),
    ('Jordan', "Jordan"),
    ('Vans', "Vans"),
    )

class Closets(models.Model):
    name = models.CharField(max_length=48)
    user = models.ForeignKey('auth.User', related_name='closets')
    total_retail_value = models.CharField(max_length=48)
    total_resale_value = models.CharField(max_length=48)
    total_profit = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Sneakers(models.Model):
    closet = models.ForeignKey(Closets, on_delete=models.CASCADE, related_name='sneakers')
    owner = models.ForeignKey('auth.User', related_name='sneakers')
    images = models.ImageField(null=True)
    brand = models.CharField(max_length=15, choices=BRAND_CHOICES, default='Nike')
    release_date = models.DateTimeField()
    purchase_date = models.DateTimeField('date purchased')
    retail_price = models.CharField(max_length=15)
    resale_value = models.CharField(max_length=15)

    def __str__(self):
        return self.brand


