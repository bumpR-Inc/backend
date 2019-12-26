from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *

class AdvertSerializer(serializers.ModelSerializer):
    org_info = serializers.SerializerMethodField(read_only=True)

    def get_org_info(self, obj):
        org = obj.org
        serializer = OrgSerializer(org)
        return serializer.data

    class Meta:
        model = Advert
        fields = (
            'pk',
            'enabled',
            'description',
            'org',
            'org_info'
        )

        read_only_fields = (
            'pk',
            'org_info'
        )


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = (
            'pk',
            # 'profile',
            'description',
        )

        read_only_fields = (
            'pk',
        )