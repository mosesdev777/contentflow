# Generated by Django 5.1 on 2024-09-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.ImageField(upload_to='social-media/icons/'),
        ),
    ]
