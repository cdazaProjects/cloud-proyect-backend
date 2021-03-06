# Generated by Django 2.1 on 2020-02-20 01:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import video_encoding.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_path', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['png'])])),
                ('url', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('begin_at', models.DateTimeField(verbose_name='date begin')),
                ('end_at', models.DateTimeField(verbose_name='date end')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveIntegerField(editable=False, null=True)),
                ('height', models.PositiveIntegerField(editable=False, null=True)),
                ('duration', models.FloatField(editable=False, null=True)),
                ('file', video_encoding.fields.VideoField(height_field='height', upload_to='', width_field='width')),
                ('status', models.CharField(default='En Proceso', max_length=50)),
                ('comment', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
            ],
        ),
    ]
