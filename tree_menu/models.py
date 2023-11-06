from django.db import models


# Create your models here.
class Menu(models.Model):
    # Меню, которое может содержать несколько пунктов меню
    title = models.CharField(max_length=255, unique=True, verbose_name='Menu title')
    slug = models.SlugField(max_length=255, verbose_name="Menu slug")

    class Meta:
        # Название модели в интерфейсе администратора
        verbose_name = 'Menu'
        # Название модели во множественном числе в интерфейсе администратора
        verbose_name_plural = 'Menus'

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    # Пункт меню, который может быть вложен в иерархическую структуру
    title = models.CharField(max_length=255, verbose_name='Menu item title')
    slug = models.SlugField(max_length=255, verbose_name="Menu item slug")

    menu = models.ForeignKey(
        Menu, blank=True, related_name='items', on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE
    )

    class Meta:
        # Название модели в интерфейсе администратора
        verbose_name = 'Menu item'
        # Название модели во множественном числе в интерфейсе администратора
        verbose_name_plural = 'Menu items'

    def __str__(self) -> str:
        return self.title
