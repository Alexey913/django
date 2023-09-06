from django.shortcuts import render, get_object_or_404
from .models import Author, Post, Comment
import logging
import datetime
from random import randint as rnd

logger = logging.getLogger(__name__)


def main(request):
    logger.info(f'Посещение главной страницы - {datetime.datetime.now()}')
    context = {'title': 'Главная', 'name': 'World'}
    return render(request, 'myapp/index.html', context)


def about(request):
    timer = datetime.datetime.now()
    logger.info(f'Посещение страницы обо мне - {timer}')
    context = {'title': 'Обо мне', 'timer': timer}
    return render(request, 'myapp/about.html', context)


def rand(request, kind, count):
    side_coin = ['Орел', 'Решка']
    if kind == 'coin':
        res_kind = 'Монета'
        result = {i: side_coin[rnd(0, 1)] for i in range(1, count+1)}
        logger.info(f'Подброшена монета - {datetime.datetime.now()}')
    elif kind == 'cube':
        res_kind = 'Кубик'
        result = {i: [rnd(1, 6)] for i in range(1, count+1)}
        logger.info(f'Брошен кубик - {datetime.datetime.now()}')
    elif kind == 'number':
        res_kind = 'Случайное число'
        result = {i: f'=={rnd(1, 100)}==' for i in range(1, count+1)}
        logger.info(f'Случайное число - {datetime.datetime.now()}')
    else:
        res_kind = 'Неудача!'
        result = {'-': 'Нет такого варианта'}
        logger.info(f'Случайное число - {datetime.datetime.now()}')
    context = {'title': res_kind, 'result': result}
    return render(request, 'myapp/random.html', context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'myapp/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.count_view += 1
    post.save()
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'myapp/post_full.html', context)
