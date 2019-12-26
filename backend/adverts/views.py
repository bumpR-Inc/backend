from rest_framework import viewsets, authentication, permissions

from .serializers import *


class AdvertView(viewsets.ModelViewSet):
    authentication_classes = () #(authentication.TokenAuthentication,)
    permission_classes = () #(permissions.IsAuthenticated,)
    serializer_class = AdvertSerializer

    def get_queryset(self):
        org = self.request.GET.get("org")
        queryset = Advert.objects.all()

        if org:
            queryset = queryset.filter(org=org)

        return queryset


class OrgView(viewsets.ModelViewSet):
    authentication_classes = () #(authentication.TokenAuthentication,)
    permission_classes = () #(permissions.IsAuthenticated,)
    serializer_class = OrgSerializer
    queryset = Org.objects.all()


    def get_queryset(self):
        profile = self.request.GET.get("profile")
        queryset = Org.objects.all()

        if profile:
            queryset.filter(profile=profile)

        return queryset