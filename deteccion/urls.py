from django.urls import path
from .views import DeteccionAPIView

urlpatterns = [
    path('detecciones/', DeteccionAPIView.as_view(), name='detecciones-api'),
]
