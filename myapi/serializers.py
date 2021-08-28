# serializers.py
from rest_framework import serializers

from .models import Divar

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Divar
        fields = ('name', 'description')