# Generated by Django 5.0.6 on 2024-07-26 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playertournament',
            name='player',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='players',
        ),
        migrations.RemoveField(
            model_name='playertournament',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='PlayerTournament',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
