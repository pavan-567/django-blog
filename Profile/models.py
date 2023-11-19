from django.db import models
from Auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null= True)
    bio = models.TextField()
    image = models.ImageField(default= 'def_cute.png', upload_to= 'profile', validators= [
        FileExtensionValidator(['png', 'jpg', 'jpeg'])
    ])
    follows = models.ManyToManyField("self", related_name= "followed_by", symmetrical= False, blank= True)
    
