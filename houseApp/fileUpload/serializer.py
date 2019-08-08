from rest_framework import routers, serializers, viewsets
from fileUpload.models import House

# House Serializer
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"