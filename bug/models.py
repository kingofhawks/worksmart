from django.db import models

# Create your models here.
class BugStatistics(models.Model):
    total = models.SmallIntegerField()
    closed = models.SmallIntegerField()
    open = models.SmallIntegerField()
    date = models.DateTimeField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Date:{} Total:{} Closed:{}'.format(self.date.date(),self.total,self.closed)


