from rest_framework import serializers
from deadstox.models import Closets, Sneakers



class SneakersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sneakers
        fields = ('id', 'url', 'name', 'closet', 'images', 'brand', 'release_date', 'purchase_date', 'retail_price', 'resale_value')


class ClosetsSerializer(serializers.HyperlinkedModelSerializer):
    sneakers = SneakersSerializer(many=True)

    class Meta:
        model = Closets
        fields = ('id', 'url', 'name', 'total_retail_value', 'total_resale_value', 'total_profit', 'sneakers')
