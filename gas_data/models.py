from django.db import models

# Create your models here.
# gas_data/models.py

class GasData(models.Model):
    end_year = models.CharField(max_length=512)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=512)
    topic = models.CharField(max_length=512)
    insight = models.CharField(max_length=512)
    url = models.CharField(max_length=512)
    region = models.CharField(max_length=512)
    start_year = models.CharField(max_length=512)
    impact = models.CharField(max_length=512)
    added = models.CharField(max_length=512)
    published = models.CharField(max_length=512)
    country = models.CharField(max_length=512)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=512)
    source = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    likelihood = models.IntegerField()
