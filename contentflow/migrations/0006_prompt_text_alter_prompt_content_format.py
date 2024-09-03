# Generated by Django 5.1 on 2024-09-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0005_alter_planning_meta_alter_prompt_channel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='content_format',
            field=models.CharField(choices=[('l', 'Long Video'), ('p', 'Post'), ('s', 'Short'), ('r', 'Reel'), ('st', 'Story')], max_length=200),
        ),
    ]
