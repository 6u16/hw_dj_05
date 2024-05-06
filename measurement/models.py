from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


# Создадим модели, делаем игру в которой есть оружие
class Sensor(models.Model):  # (models.Model) - обязательное наследование от django
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
class Measurement(models.Model):  # (models.Model) - обязательное наследование от django
    id = models.IntegerField(primary_key=True)
    id_sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)  # Внешний ключ связанный с Sensor, обращаться можно через sensor
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)  # auto_now_add=True - авто проставка даты в момент добавления данных
    image = models.ImageField(max_length=None)  # (allow_empty_file=True) - Разрешить пустые файлы(Неработает)
    
# До регистрации миграций нужно будет установить python -m pip install Pillow, требуется для ImageField
# python manage.py makemigrations
# python manage.py migrate
# python manage.py loaddata Sensors_data.json  - Загрузка данных в БД