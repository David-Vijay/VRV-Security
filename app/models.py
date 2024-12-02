from django.db import models

# Create your models here.
class crud(models.Model):
    username= models.CharField( max_length=50, null=False, blank=False)
    role = models.CharField(max_length=50)
    permission=models.CharField(max_length=50)
    status=models.CharField(max_length=50,)
    def __str__(self):
        return self.username
    