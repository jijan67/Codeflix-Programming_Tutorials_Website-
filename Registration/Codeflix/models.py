from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify  
from ckeditor.fields import RichTextField

# Create your models here.
SUBSCRIPTION = (
    ('F' , 'FREE'),
    ('M' , 'MONTHLY'),
    ('Y' , 'YEARLY'),
    )


class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)
    pro_expiry_date = models.DateField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100 , choices=SUBSCRIPTION , default='FREE')

class Course(models.Model):
    title = models.CharField(max_length=100)
    course_description = RichTextField()
    is_premium = models.BooleanField(default=False)
    course_image = models.ImageField(upload_to="course")
    slug = models.SlugField(blank=True)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption

    
    
    def save(self,*args, **kwargs): 
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    


class CourseModule(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    course_module_name = models.CharField(max_length=100)
    course_description =RichTextField()
    video_url = models.URLField(max_length=200)
    can_view = models.BooleanField(default=False)

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email