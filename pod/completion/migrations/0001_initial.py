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
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='last name / first name')),
                ('email_address', models.EmailField(blank=True, default='', max_length=254, null=True, verbose_name='mail')),
                ('role', models.CharField(choices=[('Acting roles', (('actor', 'Actor'), ('voice-over', 'Voice-over'))), ('Creative roles', (('author', 'Author'), ('designer', 'Designer'), ('editor', 'Editor'), ('writer', 'Writer'))), ('Consulting roles', (('consultant', 'Consultant'),)), ('Production roles', (('contributor', 'Contributor'), ('director', 'Director'), ('technician', 'Technician'), ('soundman', 'Soundman'))), ('Speaking roles', (('speaker', 'Speaker'),))], default='author', max_length=200, verbose_name='role')),
                ('weblink', models.URLField(blank=True, null=True, verbose_name='Web link')),
            ],
            options={
                'verbose_name': 'Contributor',
                'verbose_name_plural': 'Contributors',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=False, help_text='Document is private.', verbose_name='Private document')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='EnrichModelQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('model_type', models.CharField(default='STT', max_length=100, verbose_name='Model Type')),
                ('lang', models.CharField(choices=[('-- Frequently used languages --', (('de', 'German'), ('en', 'English'), ('ar', 'Arabic'), ('zh', 'Chinese'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian'), ('ja', 'Japanese'), ('ru', 'Russian'))), ('-- All languages --', (('ab', 'Abkhazian'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('bn', 'Bengali (Bangla)'), ('dz', 'Bhutani'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('be', 'Byelorussian (Belarusian)'), ('km', 'Cambodian'), ('ca', 'Catalan'), ('zh', 'Chinese'), ('co', 'Corsican'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('fo', 'Faeroese'), ('fa', 'Farsi'), ('fj', 'Fiji'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('gl', 'Galician'), ('gd', 'Gaelic (Scottish)'), ('gv', 'Gaelic (Manx)'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('kl', 'Greenlandic'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian Creole'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('io', 'Ido'), ('id', 'Indonesian'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiak'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('rw', 'Kinyarwanda (Ruanda)'), ('ky', 'Kirghiz'), ('rn', 'Kirundi (Rundi)'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('lo', 'Laothian'), ('la', 'Latin'), ('lv', 'Latvian (Lettish)'), ('li', 'Limburgish ( Limburger)'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mo', 'Moldavian'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('ne', 'Nepali'), ('no', 'Norwegian'), ('oc', 'Occitan'), ('or', 'Oriya'), ('om', 'Oromo (Afaan Oromo)'), ('ps', 'Pashto (Pushto)'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('qu', 'Quechua'), ('rm', 'Rhaeto-Romance'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sm', 'Samoan'), ('sg', 'Sangro'), ('sa', 'Sanskrit'), ('sr', 'Serbian'), ('sh', 'Serbo-Croatian'), ('st', 'Sesotho'), ('tn', 'Setswana'), ('sn', 'Shona'), ('ii', 'Sichuan Yi'), ('sd', 'Sindhi'), ('si', 'Sinhalese'), ('ss', 'Siswati'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili (Kiswahili)'), ('sv', 'Swedish'), ('tl', 'Tagalog'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('bo', 'Tibetan'), ('ti', 'Tigrinya'), ('to', 'Tonga'), ('ts', 'Tsonga'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Wallon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zu', 'Zulu')))], default='fr', max_length=2, verbose_name='Language')),
                ('in_treatment', models.BooleanField(default=False, verbose_name='In Treatment')),
            ],
            options={
                'verbose_name': 'Enrich model queue',
                'verbose_name_plural': 'Enrich model queues',
            },
        ),
        migrations.CreateModel(
            name='Overlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(editable=False, help_text='Used to access this instance, the "slug" is a short label containing only letters, numbers, underscore or dash top.', max_length=105, unique=True, verbose_name='Slug')),
                ('time_start', models.PositiveIntegerField(default=1, help_text='Start time of the overlay, in seconds.', verbose_name='Start time')),
                ('time_end', models.PositiveIntegerField(default=2, help_text='End time of the overlay, in seconds.', verbose_name='End time')),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('position', models.CharField(choices=[('top-left', 'top-left'), ('top', 'top'), ('top-right', 'top-right'), ('right', 'right'), ('bottom-right', 'bottom-right'), ('bottom', 'bottom'), ('bottom-left', 'bottom-left'), ('left', 'left')], default='bottom-right', help_text='Position of the overlay.', max_length=100, null=True, verbose_name='Position')),
                ('background', models.BooleanField(default=True, help_text='Show the background of the overlay.', verbose_name='Show background')),
            ],
            options={
                'verbose_name': 'Overlay',
                'verbose_name_plural': 'Overlays',
                'ordering': ['time_start'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('subtitles', 'subtitles'), ('captions', 'captions')], default='subtitles', max_length=10, verbose_name='Kind')),
                ('lang', models.CharField(choices=[('-- Frequently used languages --', (('de', 'German'), ('en', 'English'), ('ar', 'Arabic'), ('zh', 'Chinese'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian'), ('ja', 'Japanese'), ('ru', 'Russian'))), ('-- All languages --', (('ab', 'Abkhazian'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('bn', 'Bengali (Bangla)'), ('dz', 'Bhutani'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('be', 'Byelorussian (Belarusian)'), ('km', 'Cambodian'), ('ca', 'Catalan'), ('zh', 'Chinese'), ('co', 'Corsican'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('fo', 'Faeroese'), ('fa', 'Farsi'), ('fj', 'Fiji'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('gl', 'Galician'), ('gd', 'Gaelic (Scottish)'), ('gv', 'Gaelic (Manx)'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('kl', 'Greenlandic'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian Creole'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('io', 'Ido'), ('id', 'Indonesian'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiak'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('rw', 'Kinyarwanda (Ruanda)'), ('ky', 'Kirghiz'), ('rn', 'Kirundi (Rundi)'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('lo', 'Laothian'), ('la', 'Latin'), ('lv', 'Latvian (Lettish)'), ('li', 'Limburgish ( Limburger)'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mo', 'Moldavian'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('ne', 'Nepali'), ('no', 'Norwegian'), ('oc', 'Occitan'), ('or', 'Oriya'), ('om', 'Oromo (Afaan Oromo)'), ('ps', 'Pashto (Pushto)'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('qu', 'Quechua'), ('rm', 'Rhaeto-Romance'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sm', 'Samoan'), ('sg', 'Sangro'), ('sa', 'Sanskrit'), ('sr', 'Serbian'), ('sh', 'Serbo-Croatian'), ('st', 'Sesotho'), ('tn', 'Setswana'), ('sn', 'Shona'), ('ii', 'Sichuan Yi'), ('sd', 'Sindhi'), ('si', 'Sinhalese'), ('ss', 'Siswati'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili (Kiswahili)'), ('sv', 'Swedish'), ('tl', 'Tagalog'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('bo', 'Tibetan'), ('ti', 'Tigrinya'), ('to', 'Tonga'), ('ts', 'Tsonga'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Wallon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zu', 'Zulu')))], default='fr', max_length=2, verbose_name='Language')),
                ('enrich_ready', models.BooleanField(default=False, verbose_name='Enrich Ready')),
                ('src', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='podfile.customfilemodel', verbose_name='Subtitle file')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
        ),
    ]
