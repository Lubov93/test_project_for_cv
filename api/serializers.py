from product.models import User, Product, Picture
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'images']

    def create(self, validated_data):
        images = self.context.get('view').request.FILES
        product = Product.objects.create(**validated_data,
                                         author_id=1)
        for image_data in images.values():
            Picture.objects.create(product_of_id=product.id, image=image_data)
        return product

    def get_images(self, product):
        return PictureSerializer(product.Images.all(), many=True).data


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'
