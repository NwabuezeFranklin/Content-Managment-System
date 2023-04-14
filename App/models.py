from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    image = models.ImageField(upload_to='images',null=True, blank=True, default="default.jpg")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)  
    email = models.EmailField(blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)   
    about = models.TextField(blank=True, null=True, )
    is_active = models.BooleanField(default=True)
    #avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ''
        return img

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    topic = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True, null=True)
    article = RichTextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True, default="default.jpg")
    
    
    class Meta:
        ordering = ['-updated', '-created']
        #ordering = ['updated', 'created'] "this means the last object created will be last, but the similar code not commented meant the opposite."
    def __str__(self):
        return self.article
    
    
    
    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ''
        return img
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    image = models.ForeignKey(Image, on_delete=models.CASCADE,null=True,)
    #author = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        #ordering = ['updated', 'created'] "this means the last object created will be last, but the similar code not commented meant the opposite."
    def __str__(self):
        return self.text
    
    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ''
        return img
 
