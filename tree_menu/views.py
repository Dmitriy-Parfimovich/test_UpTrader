# from django.shortcuts import render
from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from tree_menu.models import Menu


# Create your views here.
class IndexPageView(TemplateView):

    # Представление индексной страницы, отображающее древовидное меню
    template_name = "tree_menu/index.html"

    def get_context_data(self, **kwargs) -> dict:

        # Получение контекстных данных для представления
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(slug='main_menu').first()
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:

        # Обработка запроса GET для индексной страницы.
        response = super().get(request, *args, **kwargs)

        # Проверка количества запросов к базе данных, выполненных в целях отладки
        print("Number of database queries: ", len(connection.queries))

        return response
