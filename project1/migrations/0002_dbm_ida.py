# Generated by Django 4.0.4 on 2022-05-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbm',
            name='ida',
            field=models.CharField(default=10, max_length=250),
        ),
    ]
