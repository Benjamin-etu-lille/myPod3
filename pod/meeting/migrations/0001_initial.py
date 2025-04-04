# Generated by Django 4.2.20 on 2025-04-03 09:48

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pod.meeting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('live', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
        ('podfile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveGateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtmp_stream_url', models.CharField(help_text='Example format: rtmp://live.univ.fr/live/name', max_length=200, verbose_name='URL of the RTMP stream')),
                ('sipmediagw_server_url', models.CharField(default='https://sipmediagw.univ.fr', help_text='Example format: https://sipmediagw.univ.fr', max_length=200, verbose_name='URL of the SIPMediaGW server')),
                ('sipmediagw_server_token', models.CharField(default='1234', help_text='Example format: 1234', max_length=25, verbose_name='Bearer token for the SIPMediaGW server.')),
                ('broadcaster', models.ForeignKey(help_text='Broadcaster in charge to perform lives.', on_delete=django.db.models.deletion.CASCADE, to='live.broadcaster', verbose_name='Broadcaster')),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Live gateway',
                'verbose_name_plural': 'Live gateways',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Meeting Name')),
                ('meeting_id', models.SlugField(editable=False, max_length=255, verbose_name='Meeting ID')),
                ('attendee_password', models.CharField(max_length=50, verbose_name='Attendee Password')),
                ('moderator_password', models.CharField(editable=False, max_length=50, verbose_name='Moderator Password')),
                ('start_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start date')),
                ('expected_duration', models.DurationField(default=datetime.timedelta(seconds=7200), help_text='Specify the duration of the meeting.', verbose_name='Meeting duration')),
                ('recurrence', models.CharField(blank=True, choices=[('', 'Choisissez la fréquence de répétition'), ('-- Fréquence --', (('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')))], help_text='Specify the recurrence of the meeting: daily, weekly, monthly or yearly', max_length=10, null=True, verbose_name='Custom recurrence')),
                ('frequency', models.PositiveIntegerField(default=1, help_text='The meeting will be repeat each time of value specify. i.e: each 3 days if recurring daily', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Repeat each time')),
                ('recurring_until', models.DateField(blank=True, help_text='Recurring meeting until the specified date', null=True, verbose_name='End date of recurring meeting')),
                ('nb_occurrences', models.PositiveIntegerField(blank=True, help_text='Recurring meeting until the specified number of occurrences', null=True, verbose_name='Number of occurrences')),
                ('weekdays', models.CharField(blank=True, help_text='Recurring meeting each day(s) specified', max_length=7, null=True, validators=[django.core.validators.RegexValidator('^[0-6]{0,7}$', message='Weekdays must contain the numbers of the active days.')], verbose_name='Day(s) of week for the meeting')),
                ('monthly_type', models.CharField(choices=[('date_day', 'Every month on this date'), ('nth_day', 'Every month on the nth week, the same day of week')], default='date_day', max_length=10)),
                ('is_restricted', models.BooleanField(default=False, help_text='If this box is checked, the meeting will only be accessible to authenticated users.', verbose_name='Restricted access')),
                ('is_running', models.BooleanField(default=False, editable=False, help_text='Indicates whether this meeting is running in BigBlueButton or not!', verbose_name='Is running')),
                ('max_participants', models.IntegerField(default=150, verbose_name='Max Participants')),
                ('welcome_text', models.TextField(default='Welcome!', verbose_name='Meeting Text in Bigbluebutton')),
                ('logout_url', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='URL to visit after user logged out')),
                ('webcam_only_for_moderators', models.BooleanField(default=False, help_text='Will cause all webcams shared by viewers during this meeting to only appear for moderators.', verbose_name='Webcam Only for moderators?')),
                ('record', models.BooleanField(default=True, help_text='Will active the recording of the meeting', verbose_name='Active record')),
                ('auto_start_recording', models.BooleanField(default=False, verbose_name='Auto Start Recording')),
                ('allow_start_stop_recording', models.BooleanField(default=True, help_text='Allow the user to start/stop recording. (default true)', verbose_name='Allow Stop/Start Recording')),
                ('guest_policy', models.CharField(blank=True, choices=[('ALWAYS_ACCEPT', 'Always accept'), ('ALWAYS_DENY', 'Always deny'), ('ASK_MODERATOR', 'Ask moderator')], help_text='Will set the guest policy for the meeting.', max_length=50, null=True, verbose_name='Guest policy')),
                ('lock_settings_disable_cam', models.BooleanField(default=False, help_text='Will prevent users from sharing their camera in the meeting.', verbose_name='Disable Camera')),
                ('lock_settings_disable_mic', models.BooleanField(default=False, help_text='Will only allow user to join listen only.', verbose_name='Disable Mic')),
                ('lock_settings_disable_private_chat', models.BooleanField(default=False, help_text='If True, will disable private chats in the meeting.', verbose_name='Disable Private chat')),
                ('lock_settings_disable_public_chat', models.BooleanField(default=False, help_text='If True, will disable public chat in the meeting.', verbose_name='Disable public chat')),
                ('lock_settings_disable_note', models.BooleanField(default=False, help_text='If True, will disable notes in the meeting.', verbose_name='Disable Note')),
                ('lock_settings_locked_layout', models.BooleanField(default=False, help_text='Will lock the layout in the meeting.', verbose_name='Locked Layout')),
                ('parent_meeting_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Parent Meeting ID')),
                ('internal_meeting_id', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='Internal Meeting ID')),
                ('voice_bridge', models.IntegerField(blank=True, default=pod.meeting.models.get_random, null=True, verbose_name='Voice Bridge')),
                ('bbb_create_time', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='BBB Create Time')),
                ('is_personal', models.BooleanField(default=False, editable=False, help_text='If this box is checked, this meeting corresponds to the user’s personal meeting room.', verbose_name='Personal meeting room')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_webinar', models.BooleanField(default=False, help_text='Do you want to start this meeting as a webinar? In such a case, you can invite presenters to join you in BigBlueButton, and listeners will have direct access to a livestream in the livestreams page.', verbose_name='Webinar mode')),
                ('enable_chat', models.BooleanField(default=False, help_text='Do you want a chat on the live page for listeners? Messages sent in this live page’s chat will end up in BigBlueButton’s public chat. This public chat will be also displayed in the live.', verbose_name='Enable chat')),
                ('additional_owners', models.ManyToManyField(blank=True, help_text='You can add additional owners to the meeting.', related_name='owners_meetings', to=settings.AUTH_USER_MODEL, verbose_name='Additional owners')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_meeting', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('restrict_access_to_groups', models.ManyToManyField(blank=True, help_text='Select one or more groups who can access to this meeting', to='authentication.accessgroup', verbose_name='Groups')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Site')),
                ('slides', models.ForeignKey(blank=True, help_text='\n        BigBlueButton will accept Office documents (.doc .docx .pptx),\n        text documents(.txt), images (.png ,.jpg) and Adobe Acrobat documents (.pdf);\n        we recommend converting documents to .pdf prior to uploading for best results.\n        Maximum size is 30 MB or 150 pages per document.\n        ', null=True, on_delete=django.db.models.deletion.CASCADE, to='podfile.customfilemodel', verbose_name='Slides')),
            ],
            options={
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meeting',
                'db_table': 'meeting',
                'ordering': ('-start_at',),
                'get_latest_by': 'start_at',
            },
        ),
        migrations.CreateModel(
            name='MeetingSessionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('moderators', models.TextField(default=[], editable=False)),
                ('viewers', models.TextField(default=[], editable=False)),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('meeting', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='meeting.meeting', verbose_name='meeting')),
            ],
            options={
                'verbose_name': 'Meeting session log',
                'verbose_name_plural': 'Meeting session logs',
                'ordering': ('meeting', '-creation_date'),
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.CreateModel(
            name='Livestream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Live not started'), (1, 'Live in progress'), (2, 'Live stopped')], default=0, verbose_name='Live status')),
                ('event', models.ForeignKey(help_text='Live event for this livestream', on_delete=django.db.models.deletion.CASCADE, to='live.event', verbose_name='Event managed for this live')),
                ('live_gateway', models.ForeignKey(help_text='Live gateway (encoder and broadcaster) that perform the livestream', on_delete=django.db.models.deletion.CASCADE, to='meeting.livegateway', verbose_name='Live gateway used for this live')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.meeting', verbose_name='Meeting')),
            ],
            options={
                'verbose_name': 'Livestream',
                'verbose_name_plural': 'Livestreams',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InternalRecording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please enter a name that will allow you to easily find this recording.', max_length=250, verbose_name='Recording name')),
                ('start_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Start date')),
                ('source_url', models.CharField(default='', help_text='Please enter the address of the recording to download. This address must match the record type selected.', max_length=500, verbose_name='Address of the recording to download')),
                ('recording_id', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Recording ID')),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meeting.meeting', verbose_name='Meeting')),
                ('owner', models.ForeignKey(blank=True, help_text='User who create this recording', limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_internal_recording', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Site')),
                ('uploaded_to_pod_by', models.ForeignKey(blank=True, help_text='User who uploaded to Pod the video file', limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploader_internal_recording', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Recording',
                'verbose_name_plural': 'Recordings',
                'ordering': ('-start_at',),
                'get_latest_by': 'start_at',
            },
        ),
        migrations.AddConstraint(
            model_name='meeting',
            constraint=models.UniqueConstraint(fields=('meeting_id', 'site'), name='meeting_unique_slug_site'),
        ),
        migrations.AddConstraint(
            model_name='meeting',
            constraint=models.CheckConstraint(check=models.Q(('recurring_until__gte', models.F('start_at__date')), ('recurring_until__isnull', True), _connector='OR'), name='recurring_until_greater_than_start'),
        ),
        migrations.AddConstraint(
            model_name='meeting',
            constraint=models.CheckConstraint(check=models.Q(('frequency__gte', 1)), name='frequency_gte_1'),
        ),
        migrations.AddConstraint(
            model_name='meeting',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('nb_occurrences__isnull', True), ('recurring_until__isnull', True)), models.Q(('nb_occurrences__isnull', False), ('recurring_until__isnull', False)), _connector='OR'), name='recurring_until_and_nb_occurrences_mutually_null_or_not'),
        ),
        migrations.AddConstraint(
            model_name='livegateway',
            constraint=models.UniqueConstraint(fields=('sipmediagw_server_url',), name='livegateway_unique_sipmediagw_server_url'),
        ),
    ]
