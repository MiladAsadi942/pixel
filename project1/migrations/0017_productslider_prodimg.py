# Generated by Django 4.0.4 on 2022-05-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0016_productslider_delete_dbm'),
    ]

    operations = [
        migrations.AddField(
            model_name='productslider',
            name='ProdImg',
            field=models.ImageField(blank=True, null=True, upload_to='%y/%m/%d'),
        ),
    ]