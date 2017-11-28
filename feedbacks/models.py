from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length = 64, null=True)
    subject = models.CharField(max_length = 64, null=True)
    message = models.TextField()
    from_email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length = 20, null=True)
    create_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
