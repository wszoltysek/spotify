# Generated by Django 2.2.7 on 2020-03-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_track_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='release_date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]
