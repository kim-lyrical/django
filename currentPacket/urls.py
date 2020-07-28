from django.urls import path
from .views import *

urlpatterns = [
    path("currentPacket/", CurrentPacketLCView.as_view()),
]