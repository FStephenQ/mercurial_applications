from django.db import models

class Post(models.Model):
	post_date = models.DateField()
	title = models.CharField(max_length=100)
	content = models.CharField()
	tags = models.ManyToManyField(Tag)


class Tag(models.Model):
	name = models.CharField(max_length=100)
	count = models.IntegerField

class Comments(models.Model):
	commentor_name = models.CharField(max_length=50)
	post_date = models.DateField()
	content = models.CharField(max_length=1024)
	parent_post = models.ForeignKey('Post',on_delete=models.CASCADE)
