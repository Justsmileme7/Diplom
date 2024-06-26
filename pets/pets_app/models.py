from django.db import models

# Create your models here.

class Pets(models.Model):
    PETS_CHOICE = (
        ('cat', 'cat'),
        ('dog', 'dog'),
        ('bird', 'bird'),
        ('rat', 'rat'),
        ('snake', 'snake'),
        ('other', 'other')
    )
    image = models.ImageField(null=True, blank=True, default=None, upload_to='photos/')
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(choices=PETS_CHOICE, default='others', max_length=100 )
    breed = models.CharField(max_length=50, unique=False)
    description = models.TextField()
    age = models.IntegerField(default=0)
    place = models.CharField(max_length=50, unique=False)
    date_of_add = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.type}'



class Feedback(models.Model):
    name = models.CharField(max_length=10)
    subject = models.TextField(max_length=30)
    context_of_comment = models.TextField(max_length=500)
    phone = models.CharField(max_length=12)


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
