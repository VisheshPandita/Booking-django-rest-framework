# Generated by Django 3.1 on 2020-11-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
