# Generated by Django 4.0.4 on 2022-05-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0020_changelogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForImgBottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img1', models.ImageField(upload_to='ForImg/')),
                ('Img2', models.ImageField(upload_to='ForImg/')),
                ('Img3', models.ImageField(upload_to='ForImg/')),
                ('Img4', models.ImageField(upload_to='ForImg/')),
                ('ImgOne', models.ImageField(upload_to='ForImg/')),
            ],
        ),
    ]
