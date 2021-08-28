# views.py
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Divar


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Divar.objects.all().order_by('name')
    serializer_class = HeroSerializer