# Generated by Django 4.0.4 on 2022-05-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0023_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='CTitle',
            field=models.CharField(max_length=10, verbose_name='عنوان'),
        ),
    ]
