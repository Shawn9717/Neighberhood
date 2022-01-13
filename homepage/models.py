from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse
from cloudinary.models import CloudinaryField
class Location(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Post model class to define post database table
    """
    name = models.CharField(max_length=400)
    location = models.ForeignKey('Location',null=True, on_delete=models.CASCADE)
      #image field
    image = CloudinaryField('image')
    #image = models.ImageField(upload_to='uploads/')
    description = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    occupants = models.ManyToManyField(User, related_name='occupants', blank=True)
    fire_department = models.IntegerField(null=True)
    hospital_contact = models.IntegerField(null=True)
    security_department = models.IntegerField(null=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('homepage:index')
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()

class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    neighborhood = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name 
