from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class BugStatistics(models.Model):
    total = models.SmallIntegerField(verbose_name=_("total"))
    closed = models.SmallIntegerField(verbose_name=_("closed"))
    open = models.SmallIntegerField(verbose_name=_("open"))
    date = models.DateTimeField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("BugStatistics")
        ordering = ['date']

    def __str__(self):
        return 'Date:{} Total:{} Closed:{}'.format(self.date.date(),self.total,self.closed)


