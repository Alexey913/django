from django.core.management.base import BaseCommand
from task_1_app.models import Post


class Command(BaseCommand):
    help = "Get post by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Post ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        post = Post.objects.get(id=id)
        self.stdout.write(f'{post}')
