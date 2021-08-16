# Generated by Django 3.2.6 on 2021-08-16 07:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plink_case', '0021_alter_validparametres_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validparametres',
            name='password',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9-_]*$', 'Only numbers, letters, underscores, dashes are allowed.')]),
        ),
    ]
