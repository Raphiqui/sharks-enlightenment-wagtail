from requests import Response
from home.models import SharkPage
from sew.serializers import SharkSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class SharkViewSet(ViewSet):
    queryset = SharkPage.objects.all()
    permission_classes = [AllowAny]

    def list(self, request):
        serializer = SharkSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = SharkSerializer(item)
        return Response(serializer.data)
