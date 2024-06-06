# Generated by Django 5.0.4 on 2024-06-04 16:17

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
