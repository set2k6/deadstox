from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
BRAND_CHOICES = (
    ('Nike', "Nike"),
    ('Adidas', "Adidas"),
    ('Jordan', "Jordan"),
    ('Vans', "Vans"),
    )

class Closets(models.Model):
    name = models.CharField(max_length=48)
    user = models.ForeignKey('auth.User', related_name='closets', null=True)
    total_retail_value = models.CharField(max_length=48)
    total_resale_value = models.CharField(max_length=48)
    total_profit = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Sneakers(models.Model):
    name = models.CharField(max_length=48, null=True)
    closet = models.ForeignKey(Closets, on_delete=models.CASCADE, related_name='sneakers')
    owner = models.ForeignKey('auth.User', related_name='sneakers', null=True)
    # highlighted = models.TextField()
    images = models.ImageField(null=True)
    brand = models.CharField(max_length=15, choices=BRAND_CHOICES, default='Nike')
    release_date = models.DateTimeField()
    purchase_date = models.DateTimeField('date purchased')
    retail_price = models.CharField(max_length=15)
    resale_value = models.CharField(max_length=15)

    def __str__(self):
        return self.brand

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = self.linenos and 'table' or False
    #     options = self.title and {'title': self.title} or {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                               full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Sneakers, self).save(*args, **kwargs)


