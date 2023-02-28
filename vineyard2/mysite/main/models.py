from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = ((0,"Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices= STATUS, default=0)
    image = models.ImageField(null = True, blank = True, upload_to= 'images/')


    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title


class prayer(models.Model):
    name = models.CharField(max_length=200)
    prayerItem = models.TextField()
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def full_name(self):
        return self.name

    def prayer_item(self):
        return self.prayerItem
    def full_prayer(self):
         return f"{self.full_name} =  {self.prayer_item} ."