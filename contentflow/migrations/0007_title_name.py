# Generated by Django 5.1 on 2024-09-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0006_alter_prompt_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]