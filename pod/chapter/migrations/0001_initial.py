# Generated by Django 4.2.20 on 2025-04-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titre')),
                ('slug', models.SlugField(editable=False, help_text='Utilisé pour accéder à cette instance, le "titre court" est une étiquette formée uniquement de lettres (non accentuées), de chiffres, de l’underscore (barre de soulignement) et du tiret.', max_length=105, unique=True, verbose_name='titre court')),
                ('time_start', models.PositiveIntegerField(default=0, help_text='Début du chapitre, en secondes.', verbose_name='Début')),
            ],
            options={
                'verbose_name': 'Chapitre',
                'verbose_name_plural': 'Chapitres',
                'ordering': ['time_start'],
            },
        ),
    ]
