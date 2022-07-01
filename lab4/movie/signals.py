from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Movie
from todo.models import Todo

@receiver(post_save, sender=Movie)
def post_save_handler(*args, **kwargs):
    # print(args)
    # print(kwargs)
    if kwargs.get('created'):
        created_object = kwargs.get('instance')
        Todo.objects.create(name=f'Automated Todo From Signal {created_object.id}', description=f'{created_object.name} Has Been Produced at {created_object.production_year}')