# Generated by Django 2.0.7 on 2018-07-05 02:25

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=140)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'document',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('address_line_1', models.TextField(blank=True, null=True)),
                ('address_line_2', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('zip', models.TextField(blank=True, null=True)),
                ('agents', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=[], size=None)),
                ('assistants', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=[], size=None)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_owner', to='homeowner_catalog.Account')),
            ],
            options={
                'db_table': 'home',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('previous_condition', models.IntegerField(blank=True, choices=[(0, 'Excellent'), (1, 'Good'), (2, 'Good enough'), (3, 'Fair'), (4, 'Poor'), (5, 'Awful'), (6, 'Unknown')], default=6, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('category', models.IntegerField(choices=[(0, 'House'), (1, 'Shed'), (2, 'Garage'), (3, 'Outside'), (4, 'Other'), (5, 'Unknown')], default=5)),
                ('items', models.ManyToManyField(related_name='item_location', to='homeowner_catalog.Item')),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('items', models.ManyToManyField(related_name='item_note', to='homeowner_catalog.Item')),
                ('location', models.ManyToManyField(related_name='location_note', to='homeowner_catalog.Location')),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='OAuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('refresh_token', models.CharField(max_length=255)),
                ('token_type', models.CharField(default='Bearer', editable=False, max_length=6)),
                ('expires_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('scope', models.CharField(default='read', max_length=255)),
            ],
            options={
                'db_table': 'oauth_token',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_photos', to='homeowner_catalog.Home')),
                ('items', models.ManyToManyField(to='homeowner_catalog.Item')),
                ('location', models.ManyToManyField(to='homeowner_catalog.Location')),
            ],
            options={
                'db_table': 'photo',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='photos',
            field=models.ManyToManyField(related_name='photo_location', to='homeowner_catalog.Photo'),
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_location', to='homeowner_catalog.Location'),
        ),
        migrations.AddField(
            model_name='document',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_documents', to='homeowner_catalog.Home'),
        ),
        migrations.AddField(
            model_name='document',
            name='items',
            field=models.ManyToManyField(blank=True, to='homeowner_catalog.Item'),
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_documents', to='homeowner_catalog.Account'),
        ),
    ]
