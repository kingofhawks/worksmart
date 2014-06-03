from django.db import models

# Create your models here.
class BugStatistics(models.Model):
    total = models.SmallIntegerField()
    closed = models.SmallIntegerField()
    open = models.SmallIntegerField()
    date = models.DateField()



