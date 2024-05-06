from rest_framework import serializers

# Для ModelSerializer импортируем нашу модель Weapon
from measurement.models import Sensor, Measurement


# Сериализатор для методов GET, POST (получение датчиков, создание датчика в БД)
class SensorSerializer(serializers.ModelSerializer):
    class Meta:  # Внутренний класс в котором будет указаны какая модель используется и её поля
        model = Sensor
        fields = ['id','name','description']
    
    
# Вариант сериализатора для создания объектов Sensors в БД
class SensorSerializer_post(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    
    def create(self, validated_data):
        """
        Create and return a new `Sensor` instance, given the validated data.
        """
        return Sensor.objects.create(**validated_data)


# Для сериализатора с подробной информацией по датчику для отображения списка измерений необходимо
# использовать вложенный сериализатор. Должен получиться примерно такой код:
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id','id_sensor','temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']