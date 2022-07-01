from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Todo
from django.core.mail import send_mail

@receiver(post_save, sender=Todo)
def post_save_handler(*args, **kwargs):
    pass
    # if kwargs.get('created'):
    #     obj = kwargs.get('instance')
    #     subject = "New Todo Created"
    #     msg = obj.description
    #     receivers = ['mahmoudfierro@gmail.com']
    #     send_mail(subject=subject, message=msg, from_email='MahmoudKamal.iti@gmail', recipient_list=receivers)
