from .models import *

from rest_framework import serializers

from django.contrib.auth import get_user_model


class AllPacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPacket
        fields = '__all__'