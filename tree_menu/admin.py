from django.contrib import admin
from tree_menu.models import MenuItem, Menu


# Register your models here.
# Декоратор для регистрации пользовательского подкласса ModelAdmin - MenuAdmin
# (вместо метода admin.site.register(Menu))
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    
    # Кастомизация веб-интерфейса Django Admin для модели MenuAdmin

    # Поля, которые отображаются в интерфейсе администратора
    list_display = ('title', 'slug')
    # Поля, по которым осуществляется поиск в интерфейсе администратора
    search_fields = ('title', 'slug')

# Декоратор для регистрации пользовательского подкласса ModelAdmin - MenuItem
# (вместо метода admin.site.register(MenuItem))
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    # Кастомизация веб-интерфейса Django Admin для модели MenuItem

    # Поля, которые отображаются в интерфейсе администратора
    list_display = ('pk', 'title', 'parent')
    # Включение фильтров в интерфейсе администратора
    list_filter = ('menu',)
    # Поля, по которым осуществляется поиск в интерфейсе администратора
    search_fields = ('title', 'slug')
    # Сортировка записей (объектов) по значению первичного ключа
    ordering = ('pk',)
    # Набор полей для страницы "изменить" интерфейса администратора
    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent'), 'title', 'slug')
            }),
    )
