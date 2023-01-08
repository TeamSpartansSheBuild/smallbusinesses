from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 


# Create your models here.
class startupModel(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    logo = models.ImageField(default='default.jpg', upload_to='startup_images',null=True,blank=True)
    name = models.CharField(max_length=50,unique=True,null=False,blank=False)
    description = models.TextField(max_length=500,null=True,blank=True)
    founded = models.IntegerField(null=False,blank=False)
    location = models.CharField(max_length=100,null=False,blank=False)
    website = models.URLField(max_length=50,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name