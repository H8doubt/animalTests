from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tests.views import AnimalTestViewSet

router = DefaultRouter()
router.register(r'animal-tests', AnimalTestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]