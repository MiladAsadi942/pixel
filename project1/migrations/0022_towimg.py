# Generated by Django 4.0.4 on 2022-05-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0021_forimgbottom'),
    ]

    operations = [
        migrations.CreateModel(
            name='TowImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imgone', models.ImageField(upload_to='TowImg/')),
                ('Imgtow', models.ImageField(upload_to='TowImg/')),
            ],
        ),
    ]