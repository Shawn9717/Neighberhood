from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    """[Profile]

    Args:
        models ([ModelClass]): [Profile model to create a user profile]

    Returns:
        [models.model]: [model class to be able to use all its properties and mine]
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_images')
    user_bio = models.CharField(max_length=30)
    date_created= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    
  