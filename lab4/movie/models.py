from django.db import models


class Movie(models.Model):
    active = models.fields.BooleanField(verbose_name='Active', default=False)
    name = models.fields.CharField(verbose_name='Movie Name', max_length=50)
    production_year = models.fields.DateField(verbose_name='Production Year', null=True)
    actors = models.ManyToManyField('actor.actor')
    director = models.ForeignKey('director.director', on_delete=models.CASCADE, null=True)
    creation_time = models.fields.DateTimeField(verbose_name="Creation Time",auto_now_add=True)
    update_time = models.fields.DateTimeField(verbose_name="Update Time", auto_now=True)

    def __str__(self):
        return self.name
