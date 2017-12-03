from django.db import models
from organizations.models import Organization

class Office(models.Model):
    city = models.CharField(max_length = 25)
    address = models.CharField(max_length = 150)
    schedule = models.CharField(max_length = 150)
    org_id = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.address

