from django.db import models

# Create your models here.
class Application(models.Model):
    app1 = models.CharField(max_length=100)
    description = models.TextField(max_length=80)
    technology = models.TextField()
    publishing_house = models.CharField(max_length=50)
    pub_date = models.DateTimeField('publication date')
