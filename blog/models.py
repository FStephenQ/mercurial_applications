from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length=100)
	count = models.IntegerField()
        description = models.CharField(max_length=1024)

class Post(models.Model):
	post_date = models.DateField()
	title = models.CharField(max_length=80)
	content = models.CharField(max_length=10000000000000000000)
	tags = models.ManyToManyField(Tag)


class Comments(models.Model):
	commentor_name = models.CharField(max_length=50)
	post_date = models.DateField()
	content = models.CharField(max_length=1024)
	parent_post = models.ForeignKey('Post',on_delete=models.CASCADE)
