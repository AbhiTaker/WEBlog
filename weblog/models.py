from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class SignUp(models.Model):
    email = models.EmailField();
    name = models.CharField(max_length = 100,blank = False)

    def __unicode__(self):
        return self.email

class Post(models.Model):

    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self) :
        return ('blog_post_detail' , () ,
                {
                    'slug' : self.slug,
                })

    def save(self,*args, **kwargs) :
        if not self.slug : 
            self.slug = slugify(self.title)                            #generating slug from title
        super(Post , self).save(*args,**kwargs)

class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
