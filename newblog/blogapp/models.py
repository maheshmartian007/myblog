from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


# Create your models here.

class CustomManager(models.Model):
	def get_queryset(self):
		return super().get_queryset().filter(status = 'published')


class Post(models.Model):

	STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))

	title = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50, unique_for_date='publish')
	author = models.ForeignKey(User, related_name='blog_posts',  on_delete=models.CASCADE)
	body = RichTextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 50, choices= STATUS_CHOICES, default='draft')
	objects = CustomManager()
	Pimage = models.ImageField(null = True, blank = True, upload_to = "images/")
	tags = TaggableManager()
	# watch = models.IntegerField()



	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
		ordering = ('-publish',)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])


#Model Related to comment section
class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments',  on_delete=models.CASCADE)
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	body = RichTextField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	active = models.BooleanField(default = True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return f'Commented by {self.name} on { self.post}' 