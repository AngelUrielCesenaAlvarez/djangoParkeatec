from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DeteccionActual

def home(request):
    return HttpResponse("¡Bienvenido al sistema de detección de vehículos!")

class DeteccionAPIView(APIView):
    def post(self, request):
        numero_de_vehiculos = request.data.get('numero_de_vehiculos')
        if numero_de_vehiculos is not None:
            deteccion = DeteccionActual.actualizar_deteccion(int(numero_de_vehiculos))
            return Response({
                'success': 'Número de vehículos actualizado',
                'nuevo_conteo': deteccion.numero_de_vehiculos
            })
        else:
            return Response({'error': 'Número de vehículos no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            deteccion = DeteccionActual.obtener_ultima_deteccion()
            return Response({'numero_de_vehiculos': deteccion.numero_de_vehiculos})
        except DeteccionActual.DoesNotExist:
            return Response({'error': 'No hay detecciones disponibles'}, status=status.HTTP_404_NOT_FOUND)
