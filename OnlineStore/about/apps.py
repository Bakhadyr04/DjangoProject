# Импортируем базовый класс конфигурации приложения из Django
from django.apps import AppConfig


# Определяем класс конфигурации приложения "about"
class AboutConfig(AppConfig):
    # Задаем тип поля для автоматического создания первичного ключа в моделях
    default_auto_field = "django.db.models.BigAutoField"

    # Указываем имя приложения. Это имя используется Django для нахождения и
    # связывания компонентов приложения.
    name = "about"

    # Задаем читаемое имя для приложения, которое будет отображаться в админке
    verbose_name = "Общая информация"
