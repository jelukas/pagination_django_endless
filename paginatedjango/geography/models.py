from django.db import models

class City(models.Model):

	name = models.CharField(max_length=140)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.name
    
