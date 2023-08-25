from django.http import HttpResponse
import logging
import datetime

logger = logging.getLogger(__name__)

def main(request):

    html = """
    <h1>Главная страница проекта Django семинара 1</h1>
    <h2>Домашнее задание к семинару № 1</h2>
    <p>Привет, мир!</p>
    """

    logger.info(f'Посещение главной страницы - {datetime.datetime.now()}')
    return HttpResponse(html)

def myself(request):

    html = """
    <h1>Страница обо мне</h1>
    <h2>Таким получилось домашнее задание к семинару № 1</h2>
    <p>Добрый день!</p>
    """
    
    logger.info(f'Посещение страницы обо мне - {datetime.datetime.now()}')
    return HttpResponse(html)