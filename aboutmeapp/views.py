from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Контроллер(представление) главной страницы"""
    html = """
    <h1>Главная</h1>
    <p>Мое первое приложение</p>
    <a href='../about/'>Обо мне</a>
    """
    return HttpResponse(html)


def about_me(request):
    """Контроллер(представление) страницы обо мне"""
    html = """
    <h1>Обо мне</h1>
    <p>Мое первое приложение</p>
    <a href='../index/'>Главная</a>
    """
    return HttpResponse(html)
