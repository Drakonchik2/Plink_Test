from django.db import models
from django.core.validators import RegexValidator

PASSWORD_REGEX = RegexValidator(r'^[a-zA-Z0-9_]+$',
                                'Only numbers, letters, underscores are allowed.')


class ValidParametres(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16, validators=[PASSWORD_REGEX])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)