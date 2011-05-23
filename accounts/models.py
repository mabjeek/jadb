from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	"""(UserProfile model)"""
	CHOICES = ((u'M', u'Male'),
			   (u'F', u'Female'),)
	user = models.OneToOneField(User, editable=False)
	gender = models.CharField(max_length=10, choices=CHOICES, default='M')
	more_info = models.TextField(blank=True)

	class Admin:
		list_display = ('user', 'gender', 'more_info')
		search_fields = ('user',)

	def __unicode__(self):
		return u"UserProfile"

		