from django.urls import path

from .views import Sensors_all, Sensor, Measurement_post

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', Sensors_all.as_view()),  # GET и POST запросы к датчикам
    path('sensors/<pk>/', Sensor.as_view()),  # GET запрос к конкретному датчику с детализацией
    path('measurements/', Measurement_post.as_view()),  # POST запрос к добавлению измерений для датчика
]
