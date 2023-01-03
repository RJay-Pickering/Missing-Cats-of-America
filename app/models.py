from django.db import models
from django.conf import settings

class KittyCats(models.Model):
	ANIMAL_TYPE = (
		("Dog", "Dog"),
		("Cat", "Cat"),
		("Bird", "Bird"),
		("Rabbit", "Rabbit"),
		("Guinea Pig", "Guinea Pig"),
		("Fish", "Fish"),
		("Reptile", "Reptile"),
		("Ferret", "Ferret"),
		("Stick Insect", "Stick Insect"),
		("Rat", "Rat"),
		("Mouse", "Mouse"),
		("Amphibian", "Amphibian"),
		("Farm Animal", "Farm Animal"),
		("Other", "Other"),
	)

	img = models.ImageField()
	name = models.CharField(max_length=200)
	missing = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	contact = models.CharField(max_length=200)
	user = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	animal = models.CharField(max_length=200, choices=ANIMAL_TYPE)
	date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name