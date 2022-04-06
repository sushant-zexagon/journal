from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)
	dob = models.DateField(null=True, blank=True)
	email = models.CharField(max_length=50,null=True,blank=True)
	password = models.CharField(max_length=100)
	status = models.CharField(max_length = 20, default = 'exists')
	image = models.ImageField(null=True,blank=True,upload_to='user/images/')
	def __str__(self) -> str:
	    return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self) -> str:
	    return self.name	

class HashTag(models.Model):
	text = models.CharField(max_length=100)
	def __str__(self) -> str:
	    return self.text	

class Entry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(null=True,blank=True,upload_to='entry/images/')
	video = models.FileField(null=True,blank=True,upload_to='entry/files/')
	text = models.TextField(null=True,blank=True)
	dop = models.DateTimeField(null=True,blank=True)
	dos = models.DateTimeField(null=True,blank=True) 
	privacy = models.CharField(max_length = 20, default = 'private')
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	hashtags = models.ManyToManyField(HashTag, null=True, blank=True)
	def __str__(self):
		return (self.user.name + ' ' + str(self.dop))


