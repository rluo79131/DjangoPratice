from django.db import models
from django.utils import timezone


class data(models.Model):
    name = models.CharField(max_length=10)
    remark = models.CharField(max_length=50, blank=True)
    modTime = models.DateTimeField(null=True)
    creTime = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "data"
