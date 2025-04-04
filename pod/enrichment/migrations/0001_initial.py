# Generated by Django 4.2.20 on 2025-04-03 09:48

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('podfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrichment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titre')),
                ('slug', models.SlugField(editable=False, help_text='Utilisé pour accéder à cette instance, le "titre court" est une étiquette formée uniquement de lettres (non accentuées), de chiffres, de l’underscore (barre de soulignement) et du tiret.', max_length=105, unique=True, verbose_name='titre court')),
                ('stop_video', models.BooleanField(default=False, help_text='La vidéo s’arrêtera à l’affichage de l’enrichissement.', verbose_name='Arrêter la vidéo')),
                ('start', models.PositiveIntegerField(default=0, help_text='Temps de début de l’affichage de l’enrichissement en secondes.', verbose_name='Début')),
                ('end', models.PositiveIntegerField(default=1, help_text='Temps de fin de l’affichage de l’enrichissement en secondes.', verbose_name='Fin')),
                ('type', models.CharField(blank=True, choices=[('image', 'image'), ('richtext', 'texte riche'), ('weblink', 'lien web'), ('document', 'document'), ('embed', 'intégrer')], max_length=10, null=True, verbose_name='Type')),
                ('richtext', tinymce.models.HTMLField(blank=True, verbose_name='Texte riche')),
                ('weblink', models.URLField(blank=True, null=True, verbose_name='Lien web')),
                ('embed', models.TextField(blank=True, help_text='Collez ici un code d’une source externe pour l’intégrer.', null=True, verbose_name='Code d’intégration')),
            ],
            options={
                'verbose_name': 'Enrichissement',
                'verbose_name_plural': 'Enrichissements',
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='EnrichmentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Groupe pour les enrichissements',
                'verbose_name_plural': 'Groupes pour les enrichissements',
                'ordering': ['video'],
            },
        ),
        migrations.CreateModel(
            name='EnrichmentVtt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='podfile.customfilemodel', verbose_name='Fichier de sous-titres')),
            ],
            options={
                'verbose_name': 'Enrichissement VTT',
                'verbose_name_plural': 'Enrichissements VTT',
                'ordering': ['video'],
            },
        ),
    ]
