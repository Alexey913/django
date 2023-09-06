from django.shortcuts import redirect, render, get_object_or_404
# from .models import Author, Post, Comment
from .forms import RandForm
import logging
import datetime
from random import randint as rnd

logger = logging.getLogger(__name__)


def rand_form(request):
    if request.method == 'POST':
        form = RandForm(request.POST)
        if form.is_valid():
            kind = form.cleaned_data['kind']
            count_tries = form.cleaned_data['count_tries']
            logger.info(f'Ввод {kind} - {count_tries} - {datetime.datetime.now()}')
            return rand(request, kind=kind, count=count_tries)
    else:
        form = RandForm()
    return render(request, 'les_app/rand_form.html', {'form': form})


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
    context = {'title': res_kind, 'result': result}
    return render(request, 'les_app/rand_result.html', context)

# def author_posts(request, author_id):
#     author = get_object_or_404(Author, pk=author_id)
#     posts = Post.objects.filter(author=author)
#     return render(request, 'myapp/author_posts.html', {'author': author, 'posts': posts})


# def post_full(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     post.count_view += 1
#     post.save()
#     comments = Comment.objects.filter(post=post)
#     context = {'post': post, 'comments': comments}
#     return render(request, 'myapp/post_full.html', context)
