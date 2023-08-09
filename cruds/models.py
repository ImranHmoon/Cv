from django.db import models

# Create your models here.
class Profile(models.Model):
    RELIGION =(
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Christian', 'Christian'),
        ('Buddhoism', 'Buddhoism'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=25)
    company = models.CharField(max_length=40,null=True,blank=True)
    university = models.CharField(max_length=40,null=True,blank=True)
    degree = models.CharField(max_length=40,null=True,blank=True)
    skills = models.CharField(max_length=40,null=True,blank=True)
    job = models.CharField(max_length=25,null=True,blank=True)
    email= models.EmailField()
    address = models.TextField(max_length=250,blank=True,null=True)
    gender = models.TextField(max_length=10,null=True,blank=True)
    religion = models.CharField(max_length=25, choices=RELIGION)
    phone_number = models.TextField(max_length=20,null=True,blank=True)
    def __str__(self):
        return str(self.name)


