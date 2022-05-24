from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import *

router = SimpleRouter()
router.register('user', UserViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
