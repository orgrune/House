from django.urls import include, path
from rest_framework import routers
from fileUpload.views import HouseViewSet

router = routers.DefaultRouter()
router.register('house', HouseViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
