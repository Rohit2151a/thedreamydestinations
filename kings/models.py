from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='pics')

class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Destinations')
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    stars = models.IntegerField()
    offer = models.BooleanField(default=False)
    place = models.CharField(max_length=100)
    days = models.IntegerField()
    nights = models.IntegerField()

class AboutUs(models.Model):
    position = models.CharField(max_length=100)
    img = models.ImageField(upload_to='AboutImg')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=10)
    date = models.CharField(max_length=100)

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField()

class Reservation(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone1 = models.IntegerField(max_length=10)
    phone2 = models.IntegerField(max_length=10)
    date = models.CharField(max_length=100)
    DestID = models.IntegerField(max_length=10)
    destination = models.CharField(max_length=100)
    From_place = models.CharField(max_length=100)
    Members = models.IntegerField(max_length=10)
    Days = models.IntegerField(max_length=10)
    Nights = models.IntegerField(max_length=10)


from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField(max_length=10)
    is_active = models.BooleanField()

    def __str__(self):
        return self.user.username

