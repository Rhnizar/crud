# Generated by Django 5.0.6 on 2024-07-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tournament', '0002_remove_playertournament_player_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_players', models.IntegerField()),
                ('round_of_16_date', models.DateField(blank=True, null=True)),
                ('quarterfinals_date', models.DateField(blank=True, null=True)),
                ('semifinals_date', models.DateField(blank=True, null=True)),
                ('final_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
