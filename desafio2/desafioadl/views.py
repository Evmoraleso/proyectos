from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Tarea, Subtarea
from .serializers import TareaSerializer, SubtareaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    @action(detail=True, methods=['post'])
    def subtareas(self, request, pk=None):
        tarea = self.get_object()
        serializer = SubtareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(id_tarea=tarea)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class SubtareaViewSet(viewsets.ModelViewSet):
    queryset = Subtarea.objects.all()
    serializer_class = SubtareaSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.eliminada = request.data.get('eliminada', instance.eliminada)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
 
@api_view(['PATCH'])
def actualizar_subtarea(request, pk):
    try:
        subtarea = Subtarea.objects.get(pk=pk)
    except Subtarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        data = request.data
        serializer = SubtareaSerializer(subtarea, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def actualizar_tarea(request, pk):
    try:
        tarea = Tarea.objects.get(pk=pk)
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        data = request.data
        serializer = TareaSerializer(tarea, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

            # Actualizar el estado de las subtareas asociadas
            if 'eliminada' in data and data['eliminada']:
                subtareas = Subtarea.objects.filter(tarea=tarea)
                for subtarea in subtareas:
                    subtarea.eliminada = True
                    subtarea.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def tarea_subtarea(request):
     return render(request, 'tarea_subtarea.html', {})