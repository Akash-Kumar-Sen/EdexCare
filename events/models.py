from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.TextField()

    def __str__(self):
        return (self.first_name+" "+self.last_name)

class Testimonial(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/testimonials',null=True ,default='')
    designation=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    title=models.CharField(max_length=500)
    document=models.FileField(upload_to='docs/resources')

    def __str__(self):
        return self.title