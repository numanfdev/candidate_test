from django.db import models

class TimeData(models.Model):
    timestamp = models.DateTimeField()
    value = models.IntegerField()

class MonthData(models.Model):
    month = models.CharField(max_length=2)
    time_data = models.ManyToManyField(TimeData)

class YearData(models.Model):
    year = models.CharField(max_length=4)
    month_data = models.ManyToManyField(MonthData)
