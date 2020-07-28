from django.urls import path
from .views import *

urlpatterns = [
    path("allPacket/", AllPacketLCView.as_view()),
]