# Generated by Django 5.1 on 2024-09-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0005_remove_planning_instagram_remove_planning_meta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='text',
            field=models.TextField(default='Texto de prueba'),
            preserve_default=False,
        ),
    ]