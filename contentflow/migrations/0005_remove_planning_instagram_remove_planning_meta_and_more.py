# Generated by Django 5.1 on 2024-09-23 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentflow', '0004_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planning',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='meta',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='status',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='tiktok',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='web',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='youtube',
        ),
        migrations.AddField(
            model_name='planning',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contentflow.channel'),
        ),
        migrations.AddField(
            model_name='planning',
            name='frecuency',
            field=models.CharField(choices=[('d', 'Dayly'), ('su', 'On Sunday'), ('sa', 'On Saturday'), ('3tw', 'Three times a week'), ('e2w', 'Every 2 weeks')], default='Dayly', max_length=200),
        ),
        migrations.AddField(
            model_name='planning',
            name='social_network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contentflow.socialmedia'),
        ),
        migrations.AddField(
            model_name='planning',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]