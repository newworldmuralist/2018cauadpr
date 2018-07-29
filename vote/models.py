from django.db import models

# Create your models here.
class Ad_tv(models.Model):
	name = models.CharField(max_length = 20)
	number = models.IntegerField(default = 0)
	result = models.IntegerField(default=0)


class Ad_viral(models.Model):
	name = models.CharField(max_length = 20)
	number = models.IntegerField(default = 0)
	result = models.IntegerField(default=0)
