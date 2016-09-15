from rest_framework import serializers
from deadstox.models import Closets, Sneakers


class ClosetsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Closets
        fields = ('id', 'url', 'name', 'total_retail_value', 'total_resale_value', 'total_profit')


class SneakersSerializer(serializers.HyperlinkedModelSerializer):

    # artists = ArtistSerializer(many=True)
    class Meta:
        model = Sneakers
        fields = ('id', 'url', 'closet', 'images', 'brand', 'release_date', 'purchase_date', 'retail_price', 'resale_value')

