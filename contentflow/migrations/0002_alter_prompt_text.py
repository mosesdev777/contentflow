# Generated by Django 5.2 on 2025-04-05 04:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
