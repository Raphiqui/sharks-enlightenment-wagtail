from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import SharkSerializer
from home.models import SharkPage


class SharksViewSet(ReadOnlyModelViewSet):
    serializer_class = SharkSerializer
    queryset = SharkPage.objects.all()
