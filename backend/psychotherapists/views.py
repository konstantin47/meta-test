from rest_framework import viewsets

from .models import Psychotherapist
from .serializers import (
    PsychotherapistSerializer,
    PsychotherapistDetailSerializer,
)


class PsychotherapistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Psychotherapist.objects.all().order_by('id')
    serializer_class = PsychotherapistSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PsychotherapistDetailSerializer
        return PsychotherapistSerializer
