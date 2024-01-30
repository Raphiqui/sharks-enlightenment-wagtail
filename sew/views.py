from requests import Response
from home.models import SharkPage
from sew.serializers import SharkSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class SharksView(generics.ListCreateAPIView):
    queryset = SharkPage.objects.all()
    serializer_class = SharkSerializer
    permission_classes = [AllowAny]
