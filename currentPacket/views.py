from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.filters import SearchFilter

class CurrentPacketLCView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer] #이게 없으면 개발자가 확인하기 편하게 보여짐 (/shop/product에서)
    queryset = CurrentPacket.objects.all() #전체 보여줌
    serializer_class = CurrentPacketSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['=id','=time','=srcip','=dstip','protocol','length','info','carve']
