from rest_framework import serializers
from .models import Tarea, Subtarea

class SubtareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtarea
        fields = ['id', 'description', 'eliminada', 'id_tarea']

class TareaSerializer(serializers.ModelSerializer):
    subtareas = SubtareaSerializer(many=True, read_only=True, source='subtarea_set')

    class Meta:
        model = Tarea
        fields = ['id', 'description', 'eliminada', 'subtareas']
