# Generated by Django 3.0.1 on 2019-12-19 18:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Player First Name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Player Last Name')),
                ('imageuri', models.URLField(verbose_name='Player Image URI')),
                ('jersey_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Jersey Number')),
                ('country', models.CharField(max_length=24, verbose_name='Player Country')),
                ('matches', models.IntegerField(verbose_name='No. of Matches Played')),
                ('run', models.IntegerField(verbose_name="Player's Run")),
                ('hishest_score', models.IntegerField(verbose_name='Highest Score')),
                ('halfcentury', models.IntegerField(verbose_name='Half Century')),
                ('century', models.IntegerField(verbose_name='Century')),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
    ]