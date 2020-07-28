"""
데이터베이스에 이렇게 내용을 저장을 할거다 하고 정하기 위해 모델을 사용
python manage.py makemigrations : 데이터베이스에 반영할 내용을 추적해서 파일 만들기
python manage.py migrate : 위에서 만든 파일을 가지고 실제 DB에 내용을 반영
"""

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CurrentPacket(models.Model):
    time = models.CharField(max_length=100)
    srcip = models.CharField(max_length=50)
    dstip = models.CharField(max_length=50)
    protocol = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    info = models.CharField(max_length=200)
    carve = models.BooleanField(default=False, verbose_name="carving")

    def __str__(self):
        return self.time
