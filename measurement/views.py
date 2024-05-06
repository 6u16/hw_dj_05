# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response  # именно такой Response возвращается в API обработчике и может возвращать только простые данные(классы не может)
from rest_framework.generics import ListCreateAPIView  # для использования GET и POST запросов через класс со спец.функцией
from rest_framework.generics import RetrieveUpdateAPIView  # Provides GET, PUT and PATCH method handlers

# Импорты для детального ответа сервера
from rest_framework import status
from rest_framework.settings import api_settings

# Наши импорты моделей и сериализаторов
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# Обработчик для GET и POST запросов к датчикам, через класс
class Sensors_all(ListCreateAPIView):  # (ListCreateAPIView) используется для GET и POST запросов
    
    queryset = Sensor.objects.all()  # Указываем от куда брать данные
    serializer_class = SensorSerializer  # С помощью чего преобразуем данные
    
    # Описываем метод POST(создание датчика):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)  # request.data - это данные в запросе POST(Content-Type: application/json) - в них инфа по новому датчику, поместив их
                                                               # в данные нашего сериализатора self.serializer_class(data=, проходим валидацию по данным if serializer.is_valid():
                                                               # и serializer.save() - записываем данные в БД
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'OK'})
        else:
            return Response({'status':'ERROR'})
    
    
    # Вариант записи данных в БД с наиболее развёрнутым ответом: (На нём понял что данные не валидируются из за того что небыло введено обязательное поле "id" в json, POST запроса)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()

    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}
        
        

# Обработчик для GET и PATCH запроса по одному конкретному датчику
class Sensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()  # Указываем от куда брать данные
    serializer_class = SensorDetailSerializer  # С помощью чего преобразуем данные
    
    # Описываем метод PATCH(обновление описания датчика):
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    


# Обработчик POST(создание измерений)
class Measurement_post(ListCreateAPIView):
    queryset = Measurement.objects.all()  # Указываем от куда брать данные
    serializer_class = MeasurementSerializer  # С помощью чего преобразуем данные
    
    # # Описываем метод POST(создание измерений с детальным ответом):      
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
    

    

    