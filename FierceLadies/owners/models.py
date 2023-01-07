from django.db import models
from startups.models import startupModel
from django.template.defaultfilters import slugify 

POSITION_CHOICES = (
    ("FOUNDER", "Founder"),
    ("CO-FOUNDER", "Co-Founder"),
    ("CEO", "Ceo"),
    )

# Create your models here.
class owner(models.Model):
    startupName = models.ForeignKey(startupModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,primary_key=True,blank=True)
    slug = models.SlugField(null=True,blank=True, unique=True)
    about = models.TextField(max_length=200,)
    position = models.CharField(max_length=10,
                                choices=POSITION_CHOICES,
                                default="CEO")
    mail = models.EmailField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name