from django.db import models

class Organization(models.Model):
    slug = models.SlugField(max_length = 10, primary_key = True)
    short_name = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 100, null=True)
    phone = models.CharField(max_length = 15, default="(000)0000000")
    reestr = models.CharField(max_length = 50, default = "000000000000")
    summa_max = models.PositiveIntegerField(default=15000)
    stavka_max = models.FloatField(default=2)
    srok_max = models.PositiveIntegerField(default=28) 
    feedback_email = models.EmailField()

    def __str__(self):
        return self.slug




