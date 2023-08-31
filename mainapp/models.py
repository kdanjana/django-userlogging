from django.db import models
from django.core import validators
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10,
            validators=[RegexValidator('^[a-zA-Z0-9.\-_]+$',
                message="Username must contain only letters, numbers, underscore, dot or dash character"
            )])
    email = models.EmailField()
    password = models.CharField(max_length=20)