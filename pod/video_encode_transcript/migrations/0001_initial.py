# Generated by Django 4.2.20 on 2025-04-03 09:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pod.video.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoRendition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.CharField(help_text='Please use the only format x. i.e.: <em>640x360</em> or <em>1280x720</em> or <em>1920x1080</em>.', max_length=50, unique=True, verbose_name='resolution')),
                ('minrate', models.CharField(help_text='Please use the only format k. i.e.: <em>300k</em> or <em>600k</em> or <em>1000k</em>.', max_length=50, verbose_name='minrate')),
                ('video_bitrate', models.CharField(help_text='Please use the only format k. i.e.: <em>300k</em> or <em>600k</em> or <em>1000k</em>.', max_length=50, verbose_name='bitrate video')),
                ('maxrate', models.CharField(help_text='Please use the only format k. i.e.: <em>300k</em> or <em>600k</em> or <em>1000k</em>.', max_length=50, verbose_name='maxrate')),
                ('encoding_resolution_threshold', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='encoding resolution threshold')),
                ('audio_bitrate', models.CharField(help_text='Please use the only format k. i.e.: <em>300k</em> or <em>600k</em> or <em>1000k</em>.', max_length=50, verbose_name='bitrate audio')),
                ('encode_mp4', models.BooleanField(default=False, verbose_name='Make a MP4 version')),
                ('sites', models.ManyToManyField(to='sites.site')),
            ],
            options={
                'verbose_name': 'rendition',
                'verbose_name_plural': 'renditions',
            },
        ),
        migrations.CreateModel(
            name='PlaylistVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('audio', 'audio'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p'), ('playlist', 'playlist')], default='360p', help_text='Merci de sélectionner un format d’encodage valide\xa0: audio 360p 480p 720p 1080p playlist', max_length=10, verbose_name='Name')),
                ('encoding_format', models.CharField(choices=[('video/mp4', 'video/mp4'), ('video/mp2t', 'video/mp2t'), ('video/webm', 'video/webm'), ('audio/mp3', 'audio/mp3'), ('audio/wav', 'audio/wav'), ('application/x-mpegURL', 'application/x-mpegURL')], default='application/x-mpegURL', help_text='Merci de sélectionner un format valide\xa0: video/mp4 video/mp2t video/webm audio/mp3 audio/wav application/x-mpegURL', max_length=22, verbose_name='Format')),
                ('source_file', models.FileField(max_length=255, upload_to=pod.video.models.get_storage_path_video, verbose_name='encoding source file')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Video Playlist',
                'verbose_name_plural': 'Video Playlists',
            },
        ),
        migrations.CreateModel(
            name='EncodingVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('audio', 'audio'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p'), ('playlist', 'playlist')], default='360p', help_text='Merci de sélectionner un format d’encodage valide\xa0: audio 360p 480p 720p 1080p playlist', max_length=10, verbose_name='Name')),
                ('encoding_format', models.CharField(choices=[('video/mp4', 'video/mp4'), ('video/mp2t', 'video/mp2t'), ('video/webm', 'video/webm'), ('audio/mp3', 'audio/mp3'), ('audio/wav', 'audio/wav'), ('application/x-mpegURL', 'application/x-mpegURL')], default='video/mp4', help_text='Merci de sélectionner un format valide\xa0: video/mp4 video/mp2t video/webm audio/mp3 audio/wav application/x-mpegURL', max_length=22, verbose_name='Format')),
                ('source_file', models.FileField(max_length=255, upload_to=pod.video.models.get_storage_path_video, verbose_name='encoding source file')),
                ('rendition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_encode_transcript.videorendition', verbose_name='rendition')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Encoding video',
                'verbose_name_plural': 'Encoding videos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EncodingStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_step', models.IntegerField(default=0, editable=False)),
                ('desc_step', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('video', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='video.video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Encoding step',
                'verbose_name_plural': 'Encoding steps',
                'ordering': ['video'],
            },
        ),
        migrations.CreateModel(
            name='EncodingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(blank=True, editable=False, null=True)),
                ('logfile', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
                ('video', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='video.video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Encoding log',
                'verbose_name_plural': 'Encoding logs',
                'ordering': ['video'],
            },
        ),
        migrations.CreateModel(
            name='EncodingAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('audio', 'audio'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p'), ('playlist', 'playlist')], default='audio', help_text='Merci de sélectionner un format d’encodage valide\xa0: audio 360p 480p 720p 1080p playlist', max_length=10, verbose_name='Name')),
                ('encoding_format', models.CharField(choices=[('video/mp4', 'video/mp4'), ('video/mp2t', 'video/mp2t'), ('video/webm', 'video/webm'), ('audio/mp3', 'audio/mp3'), ('audio/wav', 'audio/wav'), ('application/x-mpegURL', 'application/x-mpegURL')], default='audio/mp3', help_text='Merci de sélectionner un format valide\xa0: video/mp4 video/mp2t video/webm audio/mp3 audio/wav application/x-mpegURL', max_length=22, verbose_name='Format')),
                ('source_file', models.FileField(max_length=255, upload_to=pod.video.models.get_storage_path_video, verbose_name='encoding source file')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Encoding audio',
                'verbose_name_plural': 'Encoding audios',
                'ordering': ['name'],
            },
        ),
    ]
