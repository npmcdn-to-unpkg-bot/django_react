from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Note(models.Model):
	label = models.CharField(max_length=255)

	def __unicode__(self):
		return self.label