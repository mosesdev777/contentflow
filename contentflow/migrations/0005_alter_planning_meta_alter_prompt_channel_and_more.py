# Generated by Django 5.1 on 2024-09-03 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0004_account_book_prompt_subcription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='meta',
            field=models.ForeignKey(blank=True, choices=[('d', 'Dayly'), ('su', 'On Sunday'), ('sa', 'On Saturday'), ('3tw', 'Three times a week'), ('e2w', 'Every 2 weeks')], null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meta', to='contentflow.account'),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentflow.mediaplatform'),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='content_format',
            field=models.TextField(choices=[('l', 'Long Video'), ('p', 'Post'), ('s', 'Short'), ('r', 'Reel'), ('st', 'Story')]),
        ),
        migrations.AlterField(
            model_name='title',
            name='content_format',
            field=models.CharField(choices=[('lv', 'Long Video'), ('p', 'Post'), ('s', 'Short'), ('r', 'Reel'), ('st', 'Story')], default='Long Video', max_length=200),
        ),
    ]