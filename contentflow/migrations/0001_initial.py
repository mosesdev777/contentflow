# Generated by Django 5.1 on 2024-09-10 14:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('purpose', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('two_factor_authenticator', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('purpose', models.CharField(choices=[('s', 'Spirituality'), ('st', 'Stoicicim'), ('pg', 'Personal Growth'), ('f', 'Financial'), ('e', 'Education'), ('h', 'Health')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='social-media/image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upadated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, null=True)),
                ('platform', models.CharField(max_length=200)),
                ('plan', models.CharField(max_length=200)),
                ('amount', models.FloatField(default=0)),
                ('mail', models.EmailField(max_length=254)),
                ('start_date', models.DateField()),
                ('renewal', models.CharField(choices=[('y', 'Yearly'), ('m', 'Monthly'), ('e3m', 'Each 3 Months'), ('pag', 'Pay as you go')], default='Monthly', max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoiceAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('character_type', models.CharField(choices=[('s', 'Stoic'), ('ps', 'Psycologist'), ('w', 'Writer'), ('m', 'Mentor')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ManyToManyField(to='contentflow.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_used', models.BooleanField(default=False)),
                ('date_used', models.DateField(blank=True, null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentflow.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('instagram', models.ForeignKey(blank=True, choices=[('d', 'Dayly'), ('su', 'On Sunday'), ('sa', 'On Saturday'), ('3tw', 'Three times a week'), ('e2w', 'Every 2 weeks')], default='Dayly', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instagram', to='contentflow.account')),
                ('meta', models.ForeignKey(blank=True, choices=[('d', 'Dayly'), ('su', 'On Sunday'), ('sa', 'On Saturday'), ('3tw', 'Three times a week'), ('e2w', 'Every 2 weeks')], null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meta', to='contentflow.account')),
                ('tiktok', models.ForeignKey(blank=True, choices=[('d', 'Dayly'), ('su', 'On Sunday'), ('sa', 'On Saturday'), ('3tw', 'Three times a week'), ('e2w', 'Every 2 weeks')], default='Dayly', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tiktok', to='contentflow.account')),
                ('web', models.ForeignKey(blank=True, choices=[('d', 'Dayly'), ('su', 'On Sunday'), ('sa', 'On Saturday'), ('3tw', 'Three times a week'), ('e2w', 'Every 2 weeks')], default='Dayly', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web', to='contentflow.account')),
                ('youtube', models.ForeignKey(blank=True, choices=[('d', 'Dayly'), ('su', 'On Sunday'), ('sa', 'On Saturday'), ('3tw', 'Three times a week'), ('e2w', 'Every 2 weeks')], default='Dayly', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='youtube', to='contentflow.account')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users/avatars/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_format', models.CharField(choices=[('l', 'Long Video'), ('p', 'Post'), ('s', 'Short'), ('r', 'Reel'), ('st', 'Story')], max_length=200)),
                ('text', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentflow.channel')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='social_media',
            field=models.ManyToManyField(to='contentflow.socialmedia'),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content_format', models.CharField(choices=[('lv', 'Long Video'), ('p', 'Post'), ('s', 'Short'), ('r', 'Reel'), ('st', 'Story')], default='Long Video', max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentflow.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uuid', models.UUIDField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField()),
                ('script', models.TextField()),
                ('thumbnail_title', models.CharField(blank=True, max_length=200, null=True)),
                ('voice_type', models.CharField(choices=[('h', 'Human'), ('ai', 'AI')], default='Human', max_length=100)),
                ('voice_name', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('c', 'Created'), ('p', 'Published'), ('d', 'Deleted')], default='Created', max_length=100)),
                ('content_format', models.CharField(blank=True, choices=[('l', 'Long Video'), ('p', 'Post'), ('s', 'Short'), ('r', 'Reel'), ('st', 'Story')], default='Post', max_length=100)),
                ('background_music', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('published_at', models.DateField(auto_now=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentflow.channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('social_media', models.ManyToManyField(to='contentflow.socialmedia')),
                ('voice_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contentflow.voiceauthor')),
            ],
        ),
    ]
