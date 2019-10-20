"""Создадим иерархию списков маршрутов. В списке созданном у самого проекта
(Списке маршрутов уровня проекта), мы можем маршруты, которые указывают на
вложенные списки маршрутов, записанные в отдельные приложения проекта
(списки маршрутов уровня приложения). А последних мы уже запишем все
контроллеры, что составляет программную логику нашего сайта."""

from django.urls import path

from .views import index

urlpatterns = [
    path('', index), # пустая строка переданная первым параметром
] # path(),обозначает корень пути из предыдущего уровня вложения(род)
