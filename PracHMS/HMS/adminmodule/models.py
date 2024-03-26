from django.db import models
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.IntegerField()
    class Meta:
        db_table = "SignUp"



