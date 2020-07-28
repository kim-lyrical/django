from .models import *

from rest_framework import serializers

from django.contrib.auth import get_user_model


class CurrentPacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentPacket
        fields = '__all__'