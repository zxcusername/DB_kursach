# Generated by Django 4.0.2 on 2022-02-14 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_review_pub_date_alter_song_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='votes',
        ),
    ]