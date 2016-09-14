from django.db import models

# Create your models here.
class Users(models.Model):
    closets = models.ForeignKey(Closets, on_delete=models.CASCADE)

class Closets(models.Model):
    name = models.CharField(max_length=48)
    sneakers = models.ForeignKey(Sneakers, related_name='sneakers')
    total_retail_value = models.CharField(max_length=48, Null)
    total_resale_value = models.CharField(max_length=48, Null)
    total_profit = models.CharField(max_length=48, Null)

class Sneakers(models.Model):
    owner = models.ForeignKey('auth.User', related_name='sneakers')
    images = models.FilePathField.match
    BRAND_CHOICES = (
        (NIKE, "Nike"),
        (ADIDAS, "Adidas"),
        (JORDAN, "Jordan"),
        (VANS, "Vans"),
        )

    brand = models.CharField(max_length= 15, choices=BRAND_CHOICES, default=NIKE)
    release_date = models.
    purchase_date =
    retail_price =
    resale_value =










