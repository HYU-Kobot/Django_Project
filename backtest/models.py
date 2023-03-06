from django.db import models

class Parameter(models.Model):
	period_buy = models.CharField(max_length=100)
	standardDeviation_buy = models.CharField(max_length=100, null=True, default='')
	period_sell = models.CharField(max_length=100, null=True, default='')
	standardDeviation_sell = models.CharField(max_length=100, null=True, default='')

	def __int__(self):
		return self.id

# Create your models here.