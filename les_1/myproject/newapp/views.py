from django.http import HttpResponse
from random import randint as rnd
import logging
import datetime

logger = logging.getLogger(__name__)

def coin(request):
    logger.info('Подброшена монета')
    side_coin = ['Орел', 'Решка']
    result = side_coin[rnd(0,1)]
    logger.info(f'Выпадение: {result} - {datetime.datetime.now()}')
    return HttpResponse(f'<h1>{result}</h1>')


def cube(request):
    logger.info('Брошен кубик')
    side_cube = [
        '<div>-----</div><div>|---|</div><div>|-x-|</div><div>|---|</div><div>-----</div>',
        '<div>-----</div><div>|--x|</div><div>|---|</div><div>|x--|</div><div>-----</div>',
        '<div>-----</div><div>|--x|</div><div>|-x-|</div><div>|x--|</div><div>-----</div>',
        '<div>-----</div><div>|x-x|</div><div>|---|</div><div>|x-x|</div><div>-----</div>',
        '<div>-----</div><div>|x-x|</div><div>|-x-|</div><div>|x-x|</div><div>-----</div>',
        '<div>-----</div><div>|x-x|</div><div>|x-x|</div><div>|x-x|</div><div>-----</div>',
    ]
    result = rnd(0,5)
    logger.info(f'Выпадение: {result+1} - {datetime.datetime.now()}')
    return HttpResponse(f'<h1>{side_cube[result]}</h1>')

def number(request):
    title = 'Случайное число от 1 до 100'
    logger.info('Вычисляется случайное число')
    result = rnd(1,100)
    logger.info(f'{result} - {datetime.datetime.now()}')
    return HttpResponse(f'<h1>{title}</h1> <p>{result}</p>')