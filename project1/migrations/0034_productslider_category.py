# Generated by Django 4.0.4 on 2022-05-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0033_category_alter_changelogo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productslider',
            name='category',
            field=models.ManyToManyField(to='project1.category', verbose_name='دسته بندی ها'),
        ),
    ]
