import os
# Указываем приложению WSGI Django в среде реального сервера,
# какие настройки использовать
# https://djangodoc.ru/3.2/topics/settings/
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tree.settings')

import django
# Необходимо для "автономного" использования Django,
# для загрузки настроек и заполнения реестра приложений django.apps (apps.py)
# https://djangodoc.ru/3.2/topics/settings/
django.setup()

from tree_menu.models import Menu, MenuItem

# Очищает базу данных и загружает пример Меню
def load_data():
    # Удаляем существующее в базе данных Меню
    Menu.objects.filter(title="general_menu").delete()

    # Создаем новое Меню
    general_menu = Menu.objects.create(title="general_menu", slug="general_menu")

    # Создаем корневой объект "Menu"
    menu_1 = MenuItem.objects.create(title="Menu", slug="menu", menu=general_menu)

    # Создаем объекты 2-го уровня
    submenu_1 = MenuItem.objects.create(title="Submenu_1", slug="submenu_1", menu=general_menu, parent=menu_1)
    submenu_2 = MenuItem.objects.create(title="Submenu_2", slug="submenu_2", menu=general_menu, parent=menu_1)

    # Списки объектов 3-го уровня
    submenu_1_submenus = ["level_1_1", "level_1_2", "level_1_3", "level_1_4", "level_1_5",
                          "level_1_6", "level_1_7", "level_1_8", "level_1_9", "level_1_10"]
    submenu_2_submenus = ["level_2_1", "level_2_2", "level_2_3", "level_2_4", "level_2_5",
                          "level_2_6", "level_2_7", "level_2_8", "level_2_9", "level_2_10"]

    # Создаем объекты 3-го уровня
    for level in submenu_1_submenus:
        MenuItem.objects.create(title=level, slug=level.lower(), parent=submenu_1, menu=general_menu)

    # Создаем объекты 3-го уровня
    for level in submenu_2_submenus:
        MenuItem.objects.create(title=level, slug=level.lower(), parent=submenu_2, menu=general_menu)

    # Создаем объекты 4-го уровня и 5-го уровня
    for level in submenu_1_submenus + submenu_2_submenus:
        level_item = MenuItem.objects.get(title=level)

        for i in range(1, 6):
            sublevel = MenuItem.objects.create(title=f"{level}_{i}",
                                               slug=f"{level.lower()}_{i}",
                                               parent=level_item,
                                               menu=general_menu)
            for j in range(1, 4):
                MenuItem.objects.create(title=f"{level}_{i}_{j}",
                                        slug=f"{level.lower()}_{i}_{j}",
                                        parent=sublevel,
                                        menu=general_menu)
                MenuItem.objects.create(title=f"{level}_{i}_{j}",
                                        slug=f"{level.lower()}_{i}_{j}",
                                        parent=sublevel,
                                        menu=general_menu)


if __name__ == "__main__":
    load_data()
    print("Creation of the sample database Menu completed successfully")
