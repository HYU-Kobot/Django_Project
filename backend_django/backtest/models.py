from django.db import models

class Parameter(models.Model):
	params = models.IntegerField()

	def __str__(self):
		return self.name

# Create your models here.
