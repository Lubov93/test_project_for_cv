from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializers, ProductSerializer, PictureSerializer
from product.models import User, Product, Picture


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class PictureViewSet(ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
