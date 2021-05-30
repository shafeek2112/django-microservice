from django.urls import path, include

from .views import ProductViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSets, basename='product')

urlpatterns = [    
    # Viewsets (no need to mention the 'product', becaues its mentioned in router above.)
    path('',include(router.urls)),
]