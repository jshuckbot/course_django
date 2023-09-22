import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Контроллер(представление) главной страницы"""
    html = """
    <h1>Главная</h1>
    <p>Мое первое приложение</p>
    <a href='../about/'>Обо мне</a>
    """
    logger.info("Главная страница")
    return HttpResponse(html)


def about_me(request):
    """Контроллер(представление) страницы обо мне"""
    html = """
    <h1>Обо мне</h1>
    <p>Я Иван, мне 32 года. Хочу разобраться в тонкостях веб-разработки. На уровнях frontend, backend, dev</p>
    <a href='../index/'>Главная</a>
    """
    logger.info("Страница обо мне")
    return HttpResponse(html)
