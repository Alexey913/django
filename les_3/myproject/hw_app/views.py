from django.shortcuts import render, get_object_or_404
from .models import Client, Goods, Order
from datetime import date, timedelta
from random import randint as rnd


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    context = {'client': client, 'orders': orders}
    return render(request, 'hw_app/client_orders.html', context)

def orders_term(request, client_id, term):
    client = get_object_or_404(Client, pk=client_id)
    filter_date = date.today() - timedelta(days=term)
    orders = Order.objects.filter(client=client, date_create__gte=filter_date).order_by('-date_create')
    goodses = {}
    for order in orders:
        for goods in order.goods.all():
            goodses[goods]=order.date_create
    goodses = dict(sorted(goodses.items(), key = lambda kv: kv[1], reverse=True))
    context = {'client': client, 'goodses': goodses, 'term': term}
    return render(request, 'hw_app/orders_term.html', context)


def goods_description(request, goods_id):
    goods = get_object_or_404(Goods, pk=goods_id)
    return render(request, 'hw_app/goods_description.html', {'goods': goods})
