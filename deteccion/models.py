from django.db import models

class DeteccionActual(models.Model):
    numero_de_vehiculos = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def actualizar_deteccion(numero):
        deteccion = DeteccionActual.objects.create(numero_de_vehiculos=numero)
        return deteccion

    @staticmethod
    def obtener_ultima_deteccion():
        return DeteccionActual.objects.latest('fecha')
