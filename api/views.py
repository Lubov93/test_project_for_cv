from rest_framework.viewsets import ModelViewSet

from serializers import UserSerializers, ProductSerializer
from product.models import User, Product


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
