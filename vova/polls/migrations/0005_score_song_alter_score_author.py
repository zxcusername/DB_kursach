# Generated by Django 4.0.2 on 2022-02-09 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_artist_judge_score_song_delete_choice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='song',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.song'),
        ),
        migrations.AlterField(
            model_name='score',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.judge'),
        ),
    ]
