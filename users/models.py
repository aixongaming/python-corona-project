from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	address = models.CharField(default = "default", max_length = 255, verbose_name = ("address"))
	city = models.CharField(default = "default", max_length = 255, verbose_name = ("city"))
	postal = models.CharField(default = "default", max_length = 255, verbose_name = ("postal"))
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
	
	def __str__(self):
		return '{self.user.username} Profile'

