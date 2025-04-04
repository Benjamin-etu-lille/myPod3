# Generated by Django 4.2.20 on 2025-04-03 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='Prénom')),
                ('lastname', models.CharField(max_length=100, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Intervenant',
                'verbose_name_plural': 'Intervenants',
                'ordering': ['lastname', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='JobVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speaker.job', verbose_name='Fonction de l’intervenant')),
            ],
        ),
    ]
