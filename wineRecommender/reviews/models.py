from __future__ import unicode_literals

from django.db import models
import numpy as np
# Create your models here.

class Wine(models.Model):
	"""docstring for Wine"""
	# A Wine Name
	name = models.CharField(max_length=200)

	def average_rating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return np.mean(all_ratings)

	def __unicode__(self):
		return self.name
	# def __init__(self, arg):
	# 	super(Wine, self).__init__()
	# 	self.arg = arg

class Review(models.Model):
	RATING_CHOICES = (
		(1, '1'),
	    (2, '2'),
	    (3, '3'),
	    (4, '4'),
	    (5, '5'),
	)
	# Every review will be for a specific wine
	# So wine thus becomes our FK
	#  Review 10 blongs to wine 4, etc
	wine = models.ForeignKey(Wine)
	pub_date = models.DateTimeField('date published')
	# User that made the review
	user_name = models.CharField(max_length=100)
	# Text Review
	comment = models.CharField(max_length=200)
	rating = models.IntegerField(choices=RATING_CHOICES)