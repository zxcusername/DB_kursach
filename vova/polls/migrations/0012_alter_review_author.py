# Generated by Django 4.0.2 on 2022-02-17 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_song_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.dude'),
        ),
    ]
