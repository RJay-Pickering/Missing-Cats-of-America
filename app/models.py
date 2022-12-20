from django.db import models
from django.conf import settings

class KittyCats(models.Model):
	img = models.ImageField()
	name = models.CharField(max_length=200)
	missing = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	contact = models.CharField(max_length=200)
	user = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name