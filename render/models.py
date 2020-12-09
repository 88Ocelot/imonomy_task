from django.db import models


class ApiData(models.Model):
    date = models.DateTimeField(blank=True)
    client_name = models.CharField(max_length=50,
                                   default='test_client')
    provider_name = models.CharField(max_length=50)
    wons = models.IntegerField()
    revenue = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
