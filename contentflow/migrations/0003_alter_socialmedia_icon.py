# Generated by Django 5.1 on 2024-09-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0002_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.FileField(upload_to='social-media/icons/'),
        ),
    ]
