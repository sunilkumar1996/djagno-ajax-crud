from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    name = models.CharField(max_length=100, help_text="<b>User can write their name!</b>")
    email = models.EmailField(max_length=100, unique=True, help_text="<b>User can write their email!</b>")
    hobbies = models.CharField(max_length=100, help_text="<b>User can write their Hobbies!</b>")
    gender = models.CharField(max_length=16, choices=GENDER_CHOICE)

    def __str__(self):
        return self.name
