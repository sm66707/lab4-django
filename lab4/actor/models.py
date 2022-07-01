from django.db import models

class Actor(models.Model):
    # NATIONALITIES = (
    #     ('eg', 'Egyptian'),
    #     ('ksa', 'Saudi Arabian'),
    #     ('kuwait', 'Kuwait Citizen'),
    # )
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
    )
    name = models.fields.CharField(verbose_name="Actor", max_length=100)
    gender = models.fields.CharField(choices=GENDER, max_length=6, default='Male')
    # age = models.fields.IntegerField()
    # nationality = models.fields.CharField(choices=NATIONALITIES, max_length=6)
    profile_pic = models.ImageField(upload_to='actor')

    def __str__(self):
        return self.name