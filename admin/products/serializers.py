from rest_framework import serializers
from .models import Product

#  ModelSerializer (In this method, basic create and update method is already included)
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    ## This method wil overwrite the defalut save method for doing some validation.
    # def save(self):
        # pass

