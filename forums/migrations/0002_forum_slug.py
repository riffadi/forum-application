# Generated by Django 2.2.4 on 2019-08-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
