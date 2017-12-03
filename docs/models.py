from django.db import models
from organizations.models import Organization

class Doc(models.Model):
    name = models.CharField(max_length = 150)
    text = models.TextField()
    file_doc = models.FileField(null=True, blank=True)
    org_id = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
