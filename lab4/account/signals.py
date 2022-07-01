# from django.dispatch import receiver
# from django.db import models
# from django.db.models.signals import post_save, post_delete
# from django.contrib.auth.models import User
# from django.core.mail import send_mail

# @receiver(post_save, sender=User)
# def post_save_handler(sender, instance, created, **kwargs):
    # if created:
        # subject = "Welcome"
        # msg = "Welcome"
        # receivers = ['mahmoudfierro@gmail.com']
        # print(msg)
        # email = send_mail(subject=subject, message=msg, from_email='MahmoudKamal.iti@gmail', recipient_list=receivers)
        # print(email)