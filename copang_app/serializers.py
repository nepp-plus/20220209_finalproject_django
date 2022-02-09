# queryset > dict로 자동 변환 기능.

from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Users
        fields = ('id', 'name', 'email', 'phone', 'is_admin', 'image_url', 'created_at') # 우리가 원하는 항목만 내려주기