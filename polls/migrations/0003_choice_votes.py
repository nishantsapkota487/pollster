# Generated by Django 3.0.3 on 2020-03-31 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200330_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
