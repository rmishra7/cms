# Generated by Django 3.0.1 on 2019-12-22 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20191222_0505'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('-first_name',), 'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='hishest_score',
            new_name='highest_score',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team_player', to='teams.Team'),
            preserve_default=False,
        ),
    ]
